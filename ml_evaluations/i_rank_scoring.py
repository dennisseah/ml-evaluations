from typing import Any


class IRankScoring:
    def score(self, x: list[Any], y: list[Any], **kwargs) -> float: ...
