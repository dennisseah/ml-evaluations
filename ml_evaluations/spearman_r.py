from typing import Any

from scipy import stats

from ml_evaluations.i_rank_scoring import IRankScoring


class SpearmanR(IRankScoring):
    def score(self, x: list[Any], y: list[Any], **kwargs) -> float:
        return stats.spearmanr(x, y, **kwargs).statistic.astype(float)  # type: ignore
