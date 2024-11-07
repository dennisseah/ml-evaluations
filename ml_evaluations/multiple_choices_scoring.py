from typing import Any, Literal

from ml_evaluations.i_choice_scoring import IChoiceScoring


class MultipleChoiceScoring(IChoiceScoring):
    def all_or_nothing(self, answers: list[Any], correct_answers: list[Any]) -> float:
        if len(answers) != len(correct_answers):
            return 0.0

        set_answers = set(answers)
        set_correct_answers = set(correct_answers)

        return 1.0 if set_answers == set_correct_answers else 0.0

    def right_minus_wrong(
        self, answers: list[Any], correct_answers: list[Any]
    ) -> float:
        score = 0.0

        set_correct_answers = set(correct_answers)

        for answer in answers:
            if answer in set_correct_answers:
                score += 1.0
            else:
                score -= 1.0

        if score <= 0.0:
            return 0.0

        return score / len(correct_answers)

    def right_only(self, answers: list[Any], correct_answers: list[Any]) -> float:
        if len(correct_answers) == 0:
            return 0

        set_correct_answers = set(correct_answers)
        set_answers = set(answers)

        return len(set_answers.intersection(set_correct_answers)) / len(
            set_correct_answers
        )

    def score(
        self,
        answers: list[Any],
        correct_answers: list[Any],
        option: Literal["ALL_OR_NOTHING", "RIGHT_ONLY", "RIGHT_MINUS_WRONG"],
    ) -> float:
        if option == "ALL_OR_NOTHING":
            return self.all_or_nothing(answers, correct_answers)

        if option == "RIGHT_MINUS_WRONG":
            return self.right_minus_wrong(answers, correct_answers)

        if option == "RIGHT_ONLY":
            return self.right_only(answers, correct_answers)

        raise ValueError("Invalid option")
