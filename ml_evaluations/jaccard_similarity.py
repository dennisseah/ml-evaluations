from typing import Any

from ml_evaluations.i_rank_scoring import IRankScoring


class JaccardSimilarity(IRankScoring):
    def score(self, x: list[Any], y: list[Any], **kwargs) -> float:
        if len(x) != len(y):
            raise ValueError("The length of the two arrays must be equal.")

        common_items: set[Any] = set()
        total_items: set[Any] = set()
        overlap: float = 0.0
        ave_overlap: float = 0.0

        for i in range(len(x)):
            total_items.add(x[i])
            total_items.add(y[i])

            if x[i] in y[0 : i + 1]:
                common_items.add(x[i])
            if y[i] in x[0 : i + 1]:
                common_items.add(y[i])

            overlap += len(common_items) / len(total_items)
            ave_overlap = overlap / (i + 1)

        return ave_overlap
