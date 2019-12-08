from datetime import timedelta


class CompletionCalculator:
    def __init__(self, goal: timedelta):
        self.goal = goal

    def completed(self, completed: timedelta) -> float:
        return round(completed / self.goal, ndigits=4) * 100
