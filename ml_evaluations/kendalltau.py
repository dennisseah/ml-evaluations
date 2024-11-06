from typing import Any

from scipy import stats

from ml_evaluations.i_rank_scoring import IRankScoring


class KendallTau(IRankScoring):
    def score(self, x: list[Any], y: list[Any], **kwargs) -> float:
        return stats.kendalltau(x, y, **kwargs).statistic
