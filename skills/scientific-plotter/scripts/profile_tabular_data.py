#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
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
        if min(numeric_values) > 0 and max(numeric_values) / min(numeric_values) >= 100:
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


def recommendation(chart_family: str, layout: str, confidence: float, why: str, query: str, mappings: dict[str, Any]) -> dict[str, Any]:
    return {
        "chart_family": chart_family,
        "layout": layout,
        "confidence": round(confidence, 2),
        "why": why,
        "template_query": query,
        "mapping_hints": mappings,
    }


def build_recommendations(columns: list[str], rows: list[dict[str, Any]], profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_name = {profile["name"]: profile for profile in profiles}
    numeric_columns = [profile["name"] for profile in profiles if profile["role"].startswith("numeric")]
    categorical_columns = [profile["name"] for profile in profiles if profile["role"] == "categorical"]
    datetime_columns = [profile["name"] for profile in profiles if profile["role"] == "datetime"]
    x_candidates = [name for name in datetime_columns]
    x_candidates += [name for name in numeric_columns if by_name[name].get("monotonic_in_file_order")]
    x_candidates += [name for name in numeric_columns if name not in x_candidates and by_name[name]["role"] == "numeric_continuous"]
    group_candidates = [name for name in categorical_columns if 2 <= by_name[name]["unique_count"] <= 12]
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
                    {"group": categorical_columns[0], "value": numeric_columns[0], "secondary_group": categorical_columns[1] if len(categorical_columns) > 1 else None},
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
                    {"category": categorical_columns[0], "group": categorical_columns[1] if len(categorical_columns) > 1 else None, "value": numeric_columns[0]},
                )
            )

    if x_candidates and len(numeric_columns) >= 2:
        chosen_x = x_candidates[0]
        measure_columns = [name for name in numeric_columns if name != chosen_x]
        if measure_columns:
            if len(measure_columns) >= 2:
                recommendations.append(
                    recommendation(
                        "multi_panel",
                        "stacked_line_panels",
                        0.9,
                        "The table has one likely progression axis and multiple numeric responses, which is a strong fit for vertically stacked line panels.",
                        "two-panel figure with separate metrics over a shared x-axis for multiple groups",
                        {"x": chosen_x, "measures": measure_columns[:3], "group": group_candidates[0] if group_candidates else None},
                    )
                )
            recommendations.append(
                recommendation(
                    "line",
                    "single_panel",
                    0.82,
                    "A continuous or ordered x-axis is present, so a line chart is usually the clearest default for scientific trends.",
                    "scientific line chart with multiple series over a continuous x-axis",
                    {"x": chosen_x, "y": measure_columns[0], "group": group_candidates[0] if group_candidates else None},
                )
            )

    if len(numeric_columns) >= 2:
        x_name = x_candidates[0] if x_candidates else numeric_columns[0]
        y_name = next((name for name in numeric_columns if name != x_name), None)
        if y_name:
            confidence = 0.78 if x_candidates else 0.84
            why = (
                "Two numeric variables are available with no strong ordered-axis signal, so scatter is a safe structural default."
                if not x_candidates
                else "If the ordered interpretation is weak, scatter is a good fallback to avoid implying a smooth trend."
            )
            query = "scientific scatter plot comparing groups across two variables"
            recommendations.append(
                recommendation(
                    "scatter",
                    "single_panel",
                    confidence,
                    why,
                    query,
                    {"x": x_name, "y": y_name, "group": group_candidates[0] if group_candidates else None},
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

    summary = {
        "path": str(path),
        "source": source_info,
        "row_count": len(rows),
        "column_count": len(columns),
        "columns": columns,
        "column_profiles": profiles,
        "recommended_patterns": build_recommendations(columns, rows, profiles),
    }

    likely_x_columns = [
        profile["name"]
        for profile in profiles
        if profile["role"] == "datetime" or (profile["role"] == "numeric_continuous" and profile.get("monotonic_in_file_order"))
    ]
    wide_matrix_like = bool(
        profiles
        and profiles[0]["role"] == "categorical"
        and sum(1 for profile in profiles if profile["role"].startswith("numeric")) >= 4
        and len(rows) >= 4
    )
    if not likely_x_columns and not wide_matrix_like:
        numeric_continuous_columns = [profile["name"] for profile in profiles if profile["role"] == "numeric_continuous"]
        categorical_present = any(profile["role"] == "categorical" for profile in profiles)
        if len(numeric_continuous_columns) >= 2 or (len(numeric_continuous_columns) == 1 and not categorical_present):
            likely_x_columns.append(numeric_continuous_columns[0])
    summary["likely_x_columns"] = likely_x_columns
    summary["likely_group_columns"] = [
        profile["name"]
        for profile in profiles
        if profile["role"] == "categorical" and 2 <= profile["unique_count"] <= 12
    ]
    summary["numeric_measure_columns"] = [
        profile["name"]
        for profile in profiles
        if profile["role"].startswith("numeric")
    ]
    summary["likely_measure_columns"] = [
        name for name in summary["numeric_measure_columns"] if name not in summary["likely_x_columns"]
    ]
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
