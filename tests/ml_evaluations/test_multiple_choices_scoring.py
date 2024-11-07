import pytest

from ml_evaluations.multiple_choices_scoring import MultipleChoiceScoring


def test_all_or_nothing():
    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 4]

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="ALL_OR_NOTHING"
    )
    assert score == 1.0

    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 5]

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="ALL_OR_NOTHING"
    )
    assert score == 0.0

    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3]

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="ALL_OR_NOTHING"
    )
    assert score == 0.0


def test_right_minus_wrong():
    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 4]

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="RIGHT_MINUS_WRONG"
    )
    assert score == 1.0

    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 5]

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="RIGHT_MINUS_WRONG"
    )
    assert score == 0.5  # 1, 2, 3 give 3 points, 4 minus one point, then 2/4

    answers = [1, 2, 3, 4]
    correct_answers = [1]

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="RIGHT_MINUS_WRONG"
    )
    # never go negative, we should get -3
    assert score == 0

    answers = [1, 2, 3, 4]
    correct_answers = []

    score = MultipleChoiceScoring().score(
        answers, correct_answers, option="RIGHT_MINUS_WRONG"
    )
    assert score == 0


def test_right_only():
    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 4]

    score = MultipleChoiceScoring().score(answers, correct_answers, option="RIGHT_ONLY")
    assert score == 1.0

    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 5]

    score = MultipleChoiceScoring().score(answers, correct_answers, option="RIGHT_ONLY")
    assert score == 3 / 4

    answers = [1, 2, 3, 4]
    correct_answers = [1]

    score = MultipleChoiceScoring().score(answers, correct_answers, option="RIGHT_ONLY")
    assert score == 1

    answers = [1, 2, 3, 4]
    correct_answers = []

    score = MultipleChoiceScoring().score(answers, correct_answers, option="RIGHT_ONLY")
    assert score == 0


def test_invalid_option():
    answers = [1, 2, 3, 4]
    correct_answers = [1, 2, 3, 4]

    with pytest.raises(ValueError):
        MultipleChoiceScoring().score(answers, correct_answers, option="INVALID")  # type: ignore
