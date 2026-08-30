#!/usr/bin/env python3
"""Recompute the pilot's orientation-only power table.

The script uses exact noncentral t and F distributions, alpha=.05, power=.80,
equal group allocation, and no allowance for attrition, exclusions, clustering,
interactions, or multiplicity. It is an audit aid, not a final design analysis.
"""

from __future__ import annotations

from dataclasses import dataclass

from scipy.stats import f as central_f
from scipy.stats import ncf, nct, t


ALPHA = 0.05
TARGET_POWER = 0.80


@dataclass(frozen=True)
class PowerResult:
    effect: float
    per_group: int
    total: int
    achieved_power: float


def two_sample_t_power(effect: float, per_group: int) -> float:
    """Power for a two-sided independent-samples t test with equal groups."""
    degrees_freedom = 2 * per_group - 2
    noncentrality = effect * (per_group / 2) ** 0.5
    critical = t.ppf(1 - ALPHA / 2, degrees_freedom)
    return float(
        nct.sf(critical, degrees_freedom, noncentrality)
        + nct.cdf(-critical, degrees_freedom, noncentrality)
    )


def minimum_two_sample_t(effect: float) -> PowerResult:
    for per_group in range(2, 1_000_000):
        power = two_sample_t_power(effect, per_group)
        if power >= TARGET_POWER:
            return PowerResult(effect, per_group, 2 * per_group, power)
    raise RuntimeError("Search ceiling reached")


def anova_power(effect: float, groups: int, total: int) -> float:
    """Power for a fixed-effects one-way omnibus F test."""
    numerator_df = groups - 1
    denominator_df = total - groups
    noncentrality = total * effect**2
    critical = central_f.ppf(1 - ALPHA, numerator_df, denominator_df)
    return float(ncf.sf(critical, numerator_df, denominator_df, noncentrality))


def minimum_balanced_anova(effect: float, groups: int = 3) -> PowerResult:
    for per_group in range(2, 1_000_000):
        total = groups * per_group
        power = anova_power(effect, groups, total)
        if power >= TARGET_POWER:
            return PowerResult(effect, per_group, total, power)
    raise RuntimeError("Search ceiling reached")


def minimum_idealized_anova_total(effect: float, groups: int = 3) -> int:
    """Smallest mathematical N before enforcing equal integer group sizes."""
    for total in range(groups + 1, 1_000_000):
        if anova_power(effect, groups, total) >= TARGET_POWER:
            return total
    raise RuntimeError("Search ceiling reached")


def main() -> None:
    print("Two-group, two-sided independent t test")
    print("effect\tper_group\ttotal\tachieved_power")
    for effect in (0.20, 0.25, 0.30):
        result = minimum_two_sample_t(effect)
        print(
            f"{result.effect:.2f}\t{result.per_group}\t{result.total}"
            f"\t{result.achieved_power:.6f}"
        )

    print("\nThree-group one-way omnibus ANOVA")
    print("effect\tidealized_N\tbalanced_per_group\tbalanced_total\tachieved_power")
    for effect in (0.10, 0.15, 0.20):
        idealized = minimum_idealized_anova_total(effect)
        result = minimum_balanced_anova(effect)
        print(
            f"{result.effect:.2f}\t{idealized}\t{result.per_group}"
            f"\t{result.total}\t{result.achieved_power:.6f}"
        )


if __name__ == "__main__":
    main()
