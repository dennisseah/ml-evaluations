import pytest

from ml_evaluations.kendalltau import KendallTau


def test_score_1():
    x: list[float] = [1, 2, 3, 4, 5]
    y: list[float] = [1, 2, 3, 4, 5]

    scores = KendallTau().score(x, y)
    assert round(scores, 2) == 1.0


def test_score_x():
    x: list[float] = [1, 2, 3, 4, 5]
    y: list[float] = [1, 2, 3, 5, 4]

    scores = KendallTau().score(x, y)
    assert round(scores, 2) == 0.8


def test_score_diff_array_length():
    x: list[float] = [1, 2, 3, 4, 5]
    y: list[float] = [1, 2, 3]

    with pytest.raises(ValueError):
        KendallTau().score(x, y)
