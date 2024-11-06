import pytest

from ml_evaluations.jaccard_similarity import JaccardSimilarity


def test_score_1():
    x = [
        "John Doe",
        "Mary Ann",
        "Joe Smith",
        "Phil Thompson",
        "Bill Wang",
    ]
    y = [
        "Mary Ann",
        "John Doe",
        "Phil Thompson",
        "Bill Wang",
        "Mo Farah",
    ]
    scores = JaccardSimilarity().score(x, y)
    assert round(scores, 2) == 0.55


def test_score_diff_len():
    x = [
        "John Doe",
        "Mary Ann",
        "Joe Smith",
        "Phil Thompson",
        "Bill Wang",
    ]
    y = [
        "Mary Ann",
        "John Doe",
        "Phil Thompson",
        "Bill Wang",
    ]
    with pytest.raises(ValueError):
        JaccardSimilarity().score(x, y)
