from typing import Any, Literal


class IChoiceScoring:
    def score(
        self,
        answers: list[Any],
        correct_answers: list[Any],
        option: Literal["ALL_OR_NOTHING", "RIGHT_ONLY", "RIGHT_MINUS_WRONG"],
    ) -> float: ...
