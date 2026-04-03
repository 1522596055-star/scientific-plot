#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SAMPLES_ROOT = REPO_ROOT / "samples"
STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "into",
    "your",
    "when",
    "what",
    "where",
    "have",
    "need",
    "uses",
    "used",
    "using",
    "plot",
    "figure",
    "chart",
    "scientific",
    "style",
    "like",
    "looking",
    "make",
    "create",
    "show",
    "want",
    "same",
    "should",
    "main",
    "data",
    "sample",
}
ALIASES = {
    "bars": "bar",
    "categories": "category",
    "categorical": "category",
    "curves": "line",
    "curve": "line",
    "profiles": "profile",
    "points": "point",
    "markers": "marker",
    "logscale": "log",
    "logarithmic": "log",
    "box": "boxplot",
    "violins": "violin",
    "hist": "histogram",
    "bubbles": "bubble",
    "matrix": "heatmap",
    "correlation": "heatmap",
    "subplot": "subplot",
    "subplots": "subplot",
    "two-panel": "two_panel",
    "single-panel": "single_panel",
    "multi-panel": "multi_panel",
    "multi-line": "multi_line",
    "x-axis": "x_axis",
    "y-axis": "y_axis",
    "shared-x": "shared_x",
    "shared-axis": "shared_axis",
}
COMPOUND_TOKENS = {
    "single_panel",
    "two_panel",
    "multi_panel",
    "multi_line",
    "x_axis",
    "y_axis",
    "shared_x",
    "shared_axis",
}
GENERIC_AVOID_MATCH_TOKENS = {
    "axis",
    "axes",
    "x_axis",
    "y_axis",
    "line",
    "panel",
    "shared",
    "two",
    "single",
}


@dataclass
class Sample:
    sample_id: str
    category: str
    chart_type: str
    script: str
    readme: str
    output: str
    figure_group: str | None
    data_sources: list[str]
    reuse_when: list[str]
    avoid_when: list[str]
    siblings: list[str]
    curation_role: str | None
    pattern_family: str | None


def normalize_tokens(text: str) -> list[str]:
    raw_tokens = re.findall(r"[a-z0-9_+-]+", text.lower())
    tokens: list[str] = []
    for raw in raw_tokens:
        normalized = ALIASES.get(raw, raw).replace("-", "_")
        variants = [normalized]
        if "_" in normalized and normalized not in COMPOUND_TOKENS:
            variants.extend(part for part in normalized.split("_") if part)
        for variant in variants:
            candidate = ALIASES.get(variant, variant)
            if len(candidate) < 2 or candidate in STOPWORDS:
                continue
            tokens.append(candidate)
    return tokens


def extract_bullets(text: str, heading: str) -> list[str]:
    pattern = rf"## {re.escape(heading)}\n(.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, flags=re.S)
    if not match:
        return []
    block = match.group(1)
    return [line[2:].strip() for line in block.splitlines() if line.startswith("- ")]


def load_samples() -> list[Sample]:
    samples: list[Sample] = []
    for meta_path in sorted(SAMPLES_ROOT.glob("*/sample_*/meta.json")):
        sample_dir = meta_path.parent
        readme_path = sample_dir / "README.md"
        if not readme_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        readme_text = readme_path.read_text(encoding="utf-8")
        curation = meta.get("curation", {})
        samples.append(
            Sample(
                sample_id=meta["sample_id"],
                category=sample_dir.parent.name,
                chart_type=meta.get("chart_type", "unknown"),
                script=meta["script"],
                readme=meta["readme"],
                output=meta["output"],
                figure_group=meta.get("selection", {}).get("figure_group"),
                data_sources=meta.get("data_sources", []),
                reuse_when=extract_bullets(readme_text, "Reuse this sample when"),
                avoid_when=extract_bullets(readme_text, "Do not use this sample when"),
                siblings=[
                    item.strip("`")
                    for item in extract_bullets(readme_text, "Closest sibling samples")
                    if item != "None yet in this category."
                ],
                curation_role=curation.get("role"),
                pattern_family=curation.get("pattern_family"),
            )
        )
    return samples


def weighted_overlap(query: Counter[str], text: str, weight: float) -> float:
    if not text:
        return 0.0
    target = Counter(normalize_tokens(text))
    return sum(min(query[token], target[token]) for token in query) * weight


def query_has_any(query_text: str, phrases: list[str]) -> bool:
    query = query_text.lower()
    return any(phrase in query for phrase in phrases)


def heuristic_bonus(query_text: str, sample: Sample) -> tuple[float, list[str]]:
    query = query_text.lower()
    sample_reuse_text = " ".join(sample.reuse_when).lower()
    bonus = 0.0
    reasons: list[str] = []

    def add_if(condition: bool, value: float, reason: str) -> None:
        nonlocal bonus
        if condition:
            bonus += value
            reasons.append(reason)

    add_if(any(word in query for word in ["bar", "category", "sensitivity"]) and sample.category == "bar", 5.0, "bar-family heuristic")
    add_if(any(word in query for word in ["line", "profile", "trend", "scan", "inset", "multi-line", "multi line"]) and sample.category == "line", 4.5, "line-family heuristic")
    add_if(query_has_any(query, ["single-panel", "single panel", "single axis", "one axis", "overlay"]) and sample.category == "line", 5.0, "single-panel line heuristic")
    add_if(query_has_any(query, ["multi-panel", "multi panel", "subplot", "subplots", "small multiples", "stacked panels", "1x2", "2x1", "2x2", "2x3", "3x2"]) and sample.category == "multi_panel", 6.5, "multi-panel heuristic")
    add_if(any(word in query for word in ["scatter", "point", "points", "bubble"]) and sample.category == "scatter", 5.5, "scatter-family heuristic")
    add_if(any(word in query for word in ["boxplot", "violin", "histogram", "distribution"]) and sample.category == "distribution", 6.0, "distribution-family heuristic")
    add_if(any(word in query for word in ["heatmap", "matrix", "correlation"]) and sample.category == "heatmap", 7.0, "heatmap-family heuristic")
    add_if("grouped" in query and "grouped" in sample.chart_type, 4.0, "grouped-bar match")
    add_if("horizontal" in query and "horizontal" in sample.chart_type, 4.0, "horizontal-bar match")
    add_if(query_has_any(query, ["two-panel", "two panel", "top panel", "bottom panel"]) and sample.chart_type.startswith("two_panel"), 5.0, "two-panel layout match")

    sample_shared_x = (
        any(phrase in sample_reuse_text for phrase in ["shared x-axis", "same x-axis", "share the same x-axis"])
        or "shared-x" in (sample.pattern_family or "")
        or "shared_x" in sample.chart_type
    )
    add_if(query_has_any(query, ["shared x-axis", "shared x axis", "shared-x", "shared x"]) and sample_shared_x, 3.5, "shared-x layout match")
    add_if("inset" in query and any("inset" in item.lower() for item in sample.reuse_when), 3.0, "inset match")
    add_if("log" in query and ("log" in sample_reuse_text or "log" in sample.chart_type.lower()), 3.0, "log-axis match")
    add_if(any(word in query for word in ["error", "uncertainty", "spread"]) and any(word in sample_reuse_text for word in ["error", "uncertainty", "spread"]), 3.0, "uncertainty match")
    add_if("bubble" in query and "bubble" in sample_reuse_text, 5.0, "bubble match")
    add_if(sample.pattern_family == "plain-multi-line" and query_has_any(query, ["plain single-panel", "single-panel", "single panel", "multi-line", "multi line", "continuous x-axis", "continuous x axis"]), 4.0, "plain multi-line starter match")
    return bonus, reasons


def structural_penalty(query_text: str, query_counter: Counter[str], sample: Sample) -> tuple[float, list[str]]:
    query = query_text.lower()
    penalty = 0.0
    reasons: list[str] = []

    filtered_query_counter = Counter(
        {token: count for token, count in query_counter.items() if token not in GENERIC_AVOID_MATCH_TOKENS}
    )
    avoid_penalty = weighted_overlap(filtered_query_counter, " ".join(sample.avoid_when), 3.0)
    if avoid_penalty:
        penalty += avoid_penalty
        reasons.append("avoid_when penalty")

    if query_has_any(query, ["two-panel", "two panel", "top panel", "bottom panel", "shared x-axis", "shared x axis"]) and sample.category != "multi_panel":
        penalty += 4.5
        reasons.append("explicit multi-panel mismatch")
    if query_has_any(query, ["single-panel", "single panel", "single axis", "one axis", "overlay"]) and sample.category == "multi_panel":
        penalty += 6.5
        reasons.append("single-panel mismatch")
    if query_has_any(query, ["multi-line", "multi line"]) and sample.category == "multi_panel" and not query_has_any(query, ["multi-panel", "multi panel", "subplot", "subplots"]):
        penalty += 5.0
        reasons.append("multi-line is not multi-panel penalty")
    if "bubble" in query and sample.category != "scatter":
        penalty += 5.0
        reasons.append("bubble-layout mismatch")
    if any(word in query for word in ["heatmap", "matrix", "correlation"]) and sample.category != "heatmap":
        penalty += 5.0
        reasons.append("heatmap mismatch")
    if any(word in query for word in ["boxplot", "violin", "histogram", "distribution"]) and sample.category != "distribution":
        penalty += 4.0
        reasons.append("distribution-family mismatch")

    return penalty, reasons


def score_sample(query_text: str, sample: Sample) -> tuple[float, list[str]]:
    query_counter = Counter(normalize_tokens(query_text))
    reasons: list[str] = []

    score = 0.0
    score += weighted_overlap(query_counter, sample.category, 4.0)
    score += weighted_overlap(query_counter, sample.chart_type, 5.0)
    score += weighted_overlap(query_counter, " ".join(sample.reuse_when), 3.0)
    score += weighted_overlap(query_counter, sample.figure_group or "", 2.0)
    score += weighted_overlap(query_counter, sample.pattern_family or "", 2.0)

    if sample.curation_role == "canonical":
        score += 2.0
        reasons.append("canonical starter bonus")
    elif sample.curation_role == "variant":
        score -= 0.5
        reasons.append("variant specificity penalty")

    query_tokens = set(query_counter)
    if sample.pattern_family == "parameter-scan-branch-curve" and not ({"parameter", "scan", "branch", "stable", "unstable"} & query_tokens):
        score -= 2.5
        reasons.append("parameter-scan specificity penalty")
    if sample.pattern_family == "dense-dual-encoded-line" and not ({"color", "linestyle", "legend", "overlay"} & query_tokens):
        score -= 2.0
        reasons.append("dense-encoding specificity penalty")
    if sample.pattern_family == "two-panel-shared-x-with-baselines" and not ({"baseline", "reference", "control"} & query_tokens):
        score -= 8.0
        reasons.append("baseline/reference specificity penalty")

    overlap_tokens = sorted(
        {
            token
            for token in query_counter
            if token in Counter(normalize_tokens(" ".join(sample.reuse_when + [sample.chart_type, sample.category, sample.pattern_family or ""])))
        }
    )
    if overlap_tokens:
        reasons.append("matched tokens: " + ", ".join(overlap_tokens[:8]))

    bonus, bonus_reasons = heuristic_bonus(query_text, sample)
    score += bonus
    reasons.extend(bonus_reasons)

    penalty, penalty_reasons = structural_penalty(query_text, query_counter, sample)
    score -= penalty
    reasons.extend(penalty_reasons)

    return score, reasons


def sample_to_result(sample: Sample, score: float, reasons: list[str]) -> dict:
    return {
        "score": round(score, 2),
        "sample_id": sample.sample_id,
        "category": sample.category,
        "chart_type": sample.chart_type,
        "figure_group": sample.figure_group,
        "curation": {
            "role": sample.curation_role,
            "pattern_family": sample.pattern_family,
        },
        "data_sources": sample.data_sources,
        "paths": {
            "readme": sample.readme,
            "script": sample.script,
            "output": sample.output,
            "meta": str(Path(sample.readme).with_name("meta.json")),
        },
        "reuse_when": sample.reuse_when,
        "avoid_when": sample.avoid_when,
        "siblings": sample.siblings,
        "reasons": reasons,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Find relevant scientific-plot samples for a plotting request.")
    parser.add_argument("--query", required=True, help="Short English summary of the plotting requirement")
    parser.add_argument("--top", type=int, default=5, help="Number of top matches to return")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not REPO_ROOT.exists():
        raise SystemExit(f"scientific-plot repo not found: {REPO_ROOT}")

    ranked = []
    for sample in load_samples():
        score, reasons = score_sample(args.query, sample)
        ranked.append((score, sample.sample_id, sample, reasons))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    results = [sample_to_result(sample, score, reasons) for score, _, sample, reasons in ranked[: args.top]]

    print(
        json.dumps(
            {
                "query": args.query,
                "repo_root": str(REPO_ROOT),
                "results": results,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
