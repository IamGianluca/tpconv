from datetime import timedelta

import pytest

from tpconv.converter import CompletionCalculator, NoGoalError


@pytest.mark.parametrize(
    "goal,completed,expected",
    [
        (timedelta(minutes=59), timedelta(minutes=0), 0.0),
        (timedelta(hours=10), timedelta(hours=1), 10.0),
        (timedelta(hours=1), timedelta(minutes=60), 100.0),
        (timedelta(hours=1, minutes=1), timedelta(hours=1), 98.36),
        (
            timedelta(hours=1, minutes=6, seconds=14),
            timedelta(hours=1, minutes=6, seconds=0),
            99.65,
        ),
        (timedelta(hours=5), timedelta(hours=6), 120),
    ],
)
def test_time_to_minutes(goal, completed, expected):
    assert CompletionCalculator(goal).completed(completed) == expected


def test_error_if_goal_zero():
    with pytest.raises(NoGoalError):
        CompletionCalculator(goal=timedelta(seconds=0))
