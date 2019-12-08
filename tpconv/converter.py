from datetime import timedelta


class NoGoalError(Exception):
    pass


class CompletionCalculator:
    def __init__(self, goal: timedelta):
        self._validate_goal(goal)
        self.goal = goal

    def _validate_goal(self, goal: timedelta):
        if goal.seconds == 0:
            raise NoGoalError("Goal should be higher than 0 seconds")

    def completed(self, completed: timedelta) -> float:
        return round(completed / self.goal, ndigits=4) * 100
