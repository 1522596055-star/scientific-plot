#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import mean, median
from typing import Any

try:
    import pandas as pd  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    pd = None

DATE_FORMATS = [
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%m/%d/%Y",
    "%d/%m/%Y",
    "%Y-%m",
    "%Y/%m",
    "%Y-%m-%d %H:%M:%S",
    "%Y/%m/%d %H:%M:%S",
]
X_NAME_HINTS = {
    "time",
    "date",
    "year",
    "month",
    "day",
    "temperature",
    "temp",
    "pressure",
    "distance",
    "position",
    "coordinate",
    "ratio",
    "equivalence",
    "lambda",
    "phi",
    "scan",
    "index",
    "location",
    "length",
    "radius",
    "diameter",
    "x",
    "z",
}
Y_NAME_HINTS = {
    "value",
    "response",
    "yield",
    "conversion",
    "efficiency",
    "rate",
    "fraction",
    "score",
    "delay",
    "ignition",
    "emission",
    "ppm",
    "velocity",
    "temperature_rise",
}
SIZE_NAME_HINTS = {"size", "bubble", "radius", "diameter", "area", "weight"}
LOG_SCALE_HINTS = {"delay", "ignition", "lifetime", "timescale", "residence"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Profile a tabular dataset for scientific plotting.")
    parser.add_argument("path", help="Path to csv/tsv/txt/xlsx/xls file")
    parser.add_argument("--output", help="Optional JSON output path")
    return parser.parse_args()


def sniff_delimiter(path: Path) -> str:
    if path.suffix.lower() == ".tsv":
        return "\t"
    sample = path.read_text(encoding="utf-8", errors="ignore")[:8192]
    try:
        return csv.Sniffer().sniff(sample, delimiters=",;\t|").delimiter
    except Exception:
        return ","


def load_text_table(path: Path) -> tuple[list[str], list[dict[str, Any]], dict[str, Any]]:
    delimiter = sniff_delimiter(path)
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        rows = list(reader)
        columns = reader.fieldnames or []
    return columns, rows, {"format": path.suffix.lower().lstrip("."), "delimiter": delimiter}


def load_excel_table(path: Path) -> tuple[list[str], list[dict[str, Any]], dict[str, Any]]:
    if pd is None:
        raise SystemExit("Excel input requires pandas/openpyxl in the current environment.")
    frame = pd.read_excel(path)  # type: ignore[union-attr]
    frame = frame.where(frame.notna(), None)
    columns = [str(col) for col in frame.columns.tolist()]
    rows = []
    for record in frame.to_dict(orient="records"):
        rows.append({str(key): value for key, value in record.items()})
    return columns, rows, {"format": path.suffix.lower().lstrip(".")}


def load_table(path: Path) -> tuple[list[str], list[dict[str, Any]], dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv", ".txt"}:
        return load_text_table(path)
    if suffix in {".xlsx", ".xls"}:
        return load_excel_table(path)
    raise SystemExit(f"Unsupported file type: {suffix}")


def normalize_value(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "" or text.lower() in {"nan", "none", "null", "na", "n/a"}:
        return None
    return text


def try_parse_number(text: str) -> float | None:
    candidate = text.strip().replace(",", "")
    if candidate.endswith("%"):
        candidate = candidate[:-1]
    try:
        return float(candidate)
    except ValueError:
        return None


def try_parse_datetime(text: str) -> str | None:
    stripped = text.strip()
    try:
        return datetime.fromisoformat(stripped.replace("Z", "+00:00")).isoformat()
    except ValueError:
        pass
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(stripped, fmt).isoformat()
        except ValueError:
            continue
    return None


def tokenize_name(name: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", name.lower())


def has_name_hint(name: str, hints: set[str]) -> bool:
    return any(token in hints for token in tokenize_name(name))


def is_monotonic(values: list[float]) -> bool:
    if len(values) < 3:
        return False
    return all(b >= a for a, b in zip(values, values[1:])) or all(b <= a for a, b in zip(values, values[1:]))


def column_profile(name: str, values: list[Any]) -> dict[str, Any]:
    normalized = [normalize_value(value) for value in values]
    nonempty = [value for value in normalized if value is not None]
    unique_values = list(dict.fromkeys(nonempty))
    unique_count = len(set(nonempty))
    missing_count = len(values) - len(nonempty)

    profile: dict[str, Any] = {
        "name": name,
        "nonempty_count": len(nonempty),
        "missing_count": missing_count,
        "unique_count": unique_count,
        "sample_values": unique_values[:5],
    }

    if not nonempty:
        profile["role"] = "empty"
        return profile

    parsed_numbers = [try_parse_number(value) for value in nonempty]
    if all(value is not None for value in parsed_numbers):
        numeric_values = [value for value in parsed_numbers if value is not None]
        integer_like = all(float(value).is_integer() for value in numeric_values)
        role = "numeric_discrete" if integer_like and unique_count <= 12 else "numeric_continuous"
        profile.update(
            {
                "role": role,
                "numeric_min": min(numeric_values),
                "numeric_max": max(numeric_values),
                "numeric_mean": mean(numeric_values),
                "numeric_median": median(numeric_values),
                "integer_like": integer_like,
                "monotonic_in_file_order": is_monotonic(numeric_values),
            }
        )
        if min(numeric_values) > 0:
            value_ratio = max(numeric_values) / min(numeric_values)
            if value_ratio >= 20 or (value_ratio >= 8 and has_name_hint(name, LOG_SCALE_HINTS)):
                profile["log_scale_candidate"] = True
        return profile

    parsed_dates = [try_parse_datetime(value) for value in nonempty]
    if all(value is not None for value in parsed_dates):
        profile.update(
            {
                "role": "datetime",
                "datetime_min": min(parsed_dates),
                "datetime_max": max(parsed_dates),
            }
        )
        return profile

    avg_length = sum(len(value) for value in nonempty) / len(nonempty)
    unique_ratio = unique_count / max(1, len(nonempty))
    if unique_count == 1:
        profile["role"] = "constant"
    elif unique_count <= 12 or (unique_ratio <= 0.25 and avg_length < 40):
        profile["role"] = "categorical"
    else:
        profile["role"] = "text"
    return profile


def combo_counts(rows: list[dict[str, Any]], columns: list[str]) -> Counter[tuple[str | None, ...]]:
    counts: Counter[tuple[str | None, ...]] = Counter()
    for row in rows:
        key = tuple(normalize_value(row.get(column)) for column in columns)
        counts[key] += 1
    return counts


def monotonic_within_groups(rows: list[dict[str, Any]], value_column: str, group_column: str) -> bool:
    grouped: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        group_value = normalize_value(row.get(group_column))
        value_text = normalize_value(row.get(value_column))
        if group_value is None or value_text is None:
            continue
        numeric_value = try_parse_number(value_text)
        if numeric_value is None:
            continue
        grouped[group_value].append(numeric_value)

    sequences = [values for values in grouped.values() if len(values) >= 3]
    return bool(sequences) and all(is_monotonic(values) for values in sequences)


def annotate_profiles_with_groupwise_monotonicity(
    rows: list[dict[str, Any]], profiles: list[dict[str, Any]], group_candidates: list[str]
) -> None:
    if not group_candidates:
        return
    for profile in profiles:
        if not str(profile.get("role", "")).startswith("numeric"):
            continue
        profile["monotonic_within_groups"] = any(
            monotonic_within_groups(rows, profile["name"], group_column) for group_column in group_candidates
        )


def recommendation(
    chart_family: str,
    layout: str,
    confidence: float,
    why: str,
    query: str,
    mappings: dict[str, Any],
) -> dict[str, Any]:
    return {
        "chart_family": chart_family,
        "layout": layout,
        "confidence": round(confidence, 2),
        "why": why,
        "template_query": query,
        "mapping_hints": mappings,
    }


def choose_group_candidates(profiles: list[dict[str, Any]]) -> list[str]:
    return [
        profile["name"]
        for profile in profiles
        if profile["role"] == "categorical" and 2 <= profile["unique_count"] <= 12
    ]


def choose_size_candidate(profiles: list[dict[str, Any]]) -> str | None:
    candidates = [
        profile["name"]
        for profile in profiles
        if profile["role"].startswith("numeric") and has_name_hint(profile["name"], SIZE_NAME_HINTS)
    ]
    return candidates[0] if candidates else None


def score_x_candidate(profile: dict[str, Any], columns: list[str], size_candidate: str | None) -> float:
    score = 0.0
    role = profile["role"]
    if role == "datetime":
        score += 10.0
    elif role == "numeric_discrete":
        score += 5.0
    elif role == "numeric_continuous":
        score += 4.0

    if profile.get("monotonic_in_file_order"):
        score += 4.5
    if profile.get("monotonic_within_groups"):
        score += 3.5
    if columns and profile["name"] == columns[0]:
        score += 2.5
    if profile["name"] == size_candidate:
        score -= 10.0
    if profile.get("log_scale_candidate"):
        score -= 0.75
    if role == "numeric_discrete" and profile["unique_count"] >= 4:
        score += 1.5

    for token in tokenize_name(profile["name"]):
        if token in X_NAME_HINTS:
            score += 2.5
        if token in Y_NAME_HINTS:
            score -= 1.5
    return score


def ranked_x_candidates(
    columns: list[str], profiles: list[dict[str, Any]], size_candidate: str | None
) -> list[tuple[str, float]]:
    ranked = []
    for profile in profiles:
        if profile["role"] not in {"datetime", "numeric_discrete", "numeric_continuous"}:
            continue
        ranked.append((profile["name"], score_x_candidate(profile, columns, size_candidate)))
    return sorted(ranked, key=lambda item: (-item[1], item[0]))


def score_y_candidate(profile: dict[str, Any], x_name: str | None, size_candidate: str | None) -> float:
    if profile["name"] in {x_name, size_candidate}:
        return float("-inf")

    score = 0.0
    role = profile["role"]
    if role == "numeric_continuous":
        score += 5.0
    elif role == "numeric_discrete":
        score += 2.5
    if profile.get("log_scale_candidate"):
        score += 3.0

    for token in tokenize_name(profile["name"]):
        if token in Y_NAME_HINTS:
            score += 2.5
        if token in X_NAME_HINTS:
            score -= 1.0
    return score


def ranked_measure_candidates(
    profiles: list[dict[str, Any]], x_name: str | None, size_candidate: str | None
) -> list[tuple[str, float]]:
    ranked = []
    for profile in profiles:
        if not str(profile.get("role", "")).startswith("numeric"):
            continue
        score = score_y_candidate(profile, x_name, size_candidate)
        if score == float("-inf"):
            continue
        ranked.append((profile["name"], score))
    return sorted(ranked, key=lambda item: (-item[1], item[0]))


def choose_primary_group(group_candidates: list[str]) -> str | None:
    return group_candidates[0] if group_candidates else None


def build_recommendations(columns: list[str], rows: list[dict[str, Any]], profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_name = {profile["name"]: profile for profile in profiles}
    numeric_columns = [profile["name"] for profile in profiles if profile["role"].startswith("numeric")]
    categorical_columns = [profile["name"] for profile in profiles if profile["role"] == "categorical"]
    group_candidates = choose_group_candidates(profiles)
    size_candidate = choose_size_candidate(profiles)
    recommendations: list[dict[str, Any]] = []

    first_column = columns[0] if columns else None
    first_profile = by_name.get(first_column) if first_column else None
    wide_matrix_candidate = (
        first_profile is not None
        and first_profile["role"] in {"categorical", "text"}
        and len(numeric_columns) >= 4
        and len(rows) >= 4
    )
    if wide_matrix_candidate:
        return [
            recommendation(
                "heatmap",
                "single_panel",
                0.93,
                "The table looks like a labeled matrix: one row label column plus many numeric columns.",
                "annotated heatmap showing matrix values with row and column labels",
                {"row_labels": first_column, "value_columns": numeric_columns},
            )
        ]

    x_ranking = ranked_x_candidates(columns, profiles, size_candidate)
    chosen_x = x_ranking[0][0] if x_ranking else None
    measure_ranking = ranked_measure_candidates(profiles, chosen_x, size_candidate)
    measure_columns = [name for name, _ in measure_ranking]
    primary_group = choose_primary_group(group_candidates)
    primary_y = measure_columns[0] if measure_columns else None

    bubble_ready = bool(size_candidate and chosen_x and primary_y)
    if bubble_ready:
        recommendations.append(
            recommendation(
                "scatter",
                "bubble_scatter",
                0.96,
                "The table has x/y coordinates plus a dedicated size column, which is a strong match for a bubble scatter or embedding-style plot.",
                "clustered bubble scatter with color groups and marker size encoding",
                {"x": chosen_x, "y": primary_y, "size": size_candidate, "group": primary_group},
            )
        )
        recommendations.append(
            recommendation(
                "scatter",
                "single_panel",
                0.84,
                "Even without size encoding, the data reads as positioned points rather than connected trends.",
                "scientific scatter plot comparing groups across two variables",
                {"x": chosen_x, "y": primary_y, "group": primary_group},
            )
        )
        return recommendations

    if first_profile is not None and first_profile["role"] == "categorical" and 2 <= len(numeric_columns) <= 4 and len(rows) <= 20:
        recommendations.append(
            recommendation(
                "bar",
                "grouped_single_panel",
                0.9,
                "The data has one categorical axis and a small number of numeric series, which usually reads best as grouped bars.",
                "grouped bar chart comparing several conditions across categories",
                {"category": categorical_columns[0], "series_columns": numeric_columns},
            )
        )

    if len(categorical_columns) >= 1 and len(numeric_columns) == 1:
        key_columns = categorical_columns[:2]
        counts = combo_counts(rows, key_columns)
        repeated = any(count > 1 for count in counts.values())
        if repeated:
            recommendations.append(
                recommendation(
                    "distribution",
                    "boxplot",
                    0.88,
                    "There are repeated observations within groups, so showing spread is more scientific than collapsing immediately to means.",
                    "boxplot comparing raw-value distributions across categories",
                    {
                        "group": categorical_columns[0],
                        "value": numeric_columns[0],
                        "secondary_group": categorical_columns[1] if len(categorical_columns) > 1 else None,
                    },
                )
            )
        else:
            recommendations.append(
                recommendation(
                    "bar",
                    "grouped_single_panel" if len(categorical_columns) > 1 else "single_panel",
                    0.86,
                    "There appears to be one aggregated measurement per category combination, which usually fits a bar comparison.",
                    "grouped bar chart comparing conditions across categories",
                    {
                        "category": categorical_columns[0],
                        "group": categorical_columns[1] if len(categorical_columns) > 1 else None,
                        "value": numeric_columns[0],
                    },
                )
            )

    if chosen_x and primary_y:
        primary_y_profile = by_name[primary_y]
        if primary_y_profile.get("log_scale_candidate"):
            recommendations.append(
                recommendation(
                    "scatter",
                    "single_panel",
                    0.94,
                    "The response is strictly positive and spans a broad range, so a log-scale scatter is a strong scientific default.",
                    "log-scale scientific scatter plot comparing groups across one scanned variable",
                    {"x": chosen_x, "y": primary_y, "group": primary_group, "y_scale": "log"},
                )
            )
            recommendations.append(
                recommendation(
                    "line",
                    "single_panel",
                    0.89,
                    "A log-scaled line chart can work when the same grouped points should also suggest a smooth progression over the scanned x variable.",
                    "scientific line chart with log-scaled y-axis over a scanned variable",
                    {"x": chosen_x, "y": primary_y, "group": primary_group, "y_scale": "log"},
                )
            )
        elif len(measure_columns) >= 2:
            recommendations.append(
                recommendation(
                    "multi_panel",
                    "stacked_line_panels",
                    0.9,
                    "The table has one likely progression axis and multiple numeric responses, which is a strong fit for vertically stacked line panels.",
                    "two-panel figure with separate metrics over a shared x-axis for multiple groups",
                    {"x": chosen_x, "measures": measure_columns[:3], "group": primary_group},
                )
            )
            recommendations.append(
                recommendation(
                    "line",
                    "single_panel",
                    0.83,
                    "If one response should dominate, the first ranked measurement can still be shown as a simpler single-panel line chart.",
                    "plain single-panel scientific trend over one scanned variable",
                    {"x": chosen_x, "y": primary_y, "group": primary_group},
                )
            )
        else:
            recommendations.append(
                recommendation(
                    "line",
                    "single_panel",
                    0.84,
                    "A likely progression axis is present, so a line chart is a strong default for the main scientific trend.",
                    "plain single-panel multi-line scientific trend over a continuous x-axis",
                    {"x": chosen_x, "y": primary_y, "group": primary_group},
                )
            )
            recommendations.append(
                recommendation(
                    "scatter",
                    "single_panel",
                    0.79,
                    "A scatter view is a useful fallback when the points should stay explicit rather than implying a fully smooth curve.",
                    "scientific scatter plot comparing groups across two variables",
                    {"x": chosen_x, "y": primary_y, "group": primary_group},
                )
            )

    if not recommendations and len(numeric_columns) >= 2:
        fallback_x = chosen_x or numeric_columns[0]
        fallback_y = next((name for name in numeric_columns if name != fallback_x), None)
        if fallback_y:
            recommendations.append(
                recommendation(
                    "scatter",
                    "single_panel",
                    0.8,
                    "Two numeric variables are available but no stronger table pattern dominates, so scatter is the safest structural default.",
                    "scientific scatter plot comparing groups across two variables",
                    {"x": fallback_x, "y": fallback_y, "group": primary_group},
                )
            )

    unique_recommendations: list[dict[str, Any]] = []
    seen = set()
    for item in sorted(recommendations, key=lambda entry: entry["confidence"], reverse=True):
        key = (item["chart_family"], item["layout"], item["template_query"])
        if key in seen:
            continue
        seen.add(key)
        unique_recommendations.append(item)
    return unique_recommendations[:4]


def summarize_dataset(path: Path) -> dict[str, Any]:
    columns, rows, source_info = load_table(path)
    profiles = [column_profile(column, [row.get(column) for row in rows]) for column in columns]
    group_candidates = choose_group_candidates(profiles)
    annotate_profiles_with_groupwise_monotonicity(rows, profiles, group_candidates)

    size_candidate = choose_size_candidate(profiles)
    x_ranking = ranked_x_candidates(columns, profiles, size_candidate)
    chosen_x = x_ranking[0][0] if x_ranking else None
    measure_ranking = ranked_measure_candidates(profiles, chosen_x, size_candidate)

    summary = {
        "path": str(path),
        "source": source_info,
        "row_count": len(rows),
        "column_count": len(columns),
        "columns": columns,
        "column_profiles": profiles,
        "recommended_patterns": build_recommendations(columns, rows, profiles),
        "likely_x_columns": [name for name, score in x_ranking[:2] if score > 0],
        "likely_group_columns": group_candidates,
        "likely_size_columns": [size_candidate] if size_candidate else [],
        "numeric_measure_columns": [
            profile["name"]
            for profile in profiles
            if str(profile.get("role", "")).startswith("numeric")
        ],
        "likely_measure_columns": [name for name, _ in measure_ranking[:3]],
    }
    return summary


def main() -> None:
    args = parse_args()
    path = Path(args.path).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    summary = summarize_dataset(path)
    text = json.dumps(summary, indent=2, ensure_ascii=False)
    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
