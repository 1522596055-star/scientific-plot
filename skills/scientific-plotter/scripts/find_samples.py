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
    "axis",
    "axes",
    "panel",
    "panels",
    "sample",
}
ALIASES = {
    "bars": "bar",
    "grouped": "grouped",
    "categories": "category",
    "categorical": "category",
    "subplot": "panel",
    "subplots": "panel",
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
    raw = re.findall(r"[a-z0-9_+-]+", text.lower())
    tokens: list[str] = []
    for token in raw:
        normalized = ALIASES.get(token, token)
        if len(normalized) < 2 or normalized in STOPWORDS:
            continue
        tokens.append(normalized)
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
                siblings=[item.strip("`") for item in extract_bullets(readme_text, "Closest sibling samples") if item != "None yet in this category."],
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


def heuristic_bonus(query_text: str, sample: Sample) -> tuple[float, list[str]]:
    query = query_text.lower()
    bonus = 0.0
    reasons: list[str] = []

    def add_if(condition: bool, value: float, reason: str) -> None:
        nonlocal bonus
        if condition:
            bonus += value
            reasons.append(reason)

    add_if(any(word in query for word in ["bar", "category", "sensitivity"]) and sample.category == "bar", 5.0, "bar-family heuristic")
    add_if(any(word in query for word in ["line", "profile", "trend", "scan", "inset"]) and sample.category == "line", 5.0, "line-family heuristic")
    add_if(any(word in query for word in ["multi", "subplot", "subplots", "panel", "2x", "3x"]) and sample.category == "multi_panel", 6.0, "multi-panel heuristic")
    add_if(any(word in query for word in ["scatter", "point", "points", "bubble"]) and sample.category == "scatter", 5.0, "scatter-family heuristic")
    add_if(any(word in query for word in ["boxplot", "violin", "histogram", "distribution"]) and sample.category == "distribution", 6.0, "distribution-family heuristic")
    add_if(any(word in query for word in ["heatmap", "matrix", "correlation"]) and sample.category == "heatmap", 7.0, "heatmap-family heuristic")
    add_if("grouped" in query and "grouped" in sample.chart_type, 4.0, "grouped-bar match")
    add_if("horizontal" in query and "horizontal" in sample.chart_type, 4.0, "horizontal-bar match")
    add_if(any(word in query for word in ["two-panel", "two panel", "stacked panels", "top panel", "bottom panel"]) and sample.chart_type.startswith("two_panel"), 4.0, "two-panel layout match")
    add_if("inset" in query and any("inset" in item.lower() for item in sample.reuse_when), 3.0, "inset match")
    add_if("log" in query and ("log" in " ".join(sample.reuse_when).lower() or "log" in sample.chart_type.lower()), 3.0, "log-axis match")
    add_if(any(word in query for word in ["error", "uncertainty"]) and "error" in " ".join(sample.reuse_when).lower(), 3.0, "error-bar match")
    add_if("bubble" in query and "bubble" in " ".join(sample.reuse_when).lower(), 4.0, "bubble match")
    return bonus, reasons


def score_sample(query_text: str, sample: Sample) -> tuple[float, list[str]]:
    query_counter = Counter(normalize_tokens(query_text))
    reasons: list[str] = []

    score = 0.0
    score += weighted_overlap(query_counter, sample.category.replace("_", " "), 4.0)
    score += weighted_overlap(query_counter, sample.chart_type.replace("_", " "), 5.0)
    score += weighted_overlap(query_counter, " ".join(sample.reuse_when), 3.0)
    score += weighted_overlap(query_counter, sample.figure_group or "", 2.0)
    score += weighted_overlap(query_counter, (sample.pattern_family or "").replace("-", " "), 2.0)

    if sample.curation_role == "canonical":
        score += 1.5
        reasons.append("canonical starter bonus")

    query_tokens = set(query_counter)
    if sample.pattern_family == "parameter-scan-branch-curve" and not ({"parameter", "scan", "branch", "stable", "unstable"} & query_tokens):
        score -= 2.5
        reasons.append("parameter-scan specificity penalty")
    if sample.pattern_family == "dense-dual-encoded-line" and not ({"color", "linestyle", "legend", "overlay"} & query_tokens):
        score -= 2.0
        reasons.append("dense-encoding specificity penalty")

    overlap_tokens = sorted({token for token in query_counter if token in Counter(normalize_tokens(' '.join(sample.reuse_when + [sample.chart_type, sample.category, sample.pattern_family or ''])))})
    if overlap_tokens:
        reasons.append("matched tokens: " + ", ".join(overlap_tokens[:8]))

    bonus, bonus_reasons = heuristic_bonus(query_text, sample)
    score += bonus
    reasons.extend(bonus_reasons)
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
