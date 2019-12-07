import pytest
from datetime import timedelta


@pytest.mark.parametrize(
    "time,expected",
    [
        (timedelta(minutes=59), 59),
        (timedelta(hours=1), 60),
        (timedelta(hours=1, minutes=1), 61),
        (
            timedelta(hours=1, minutes=6, seconds=14),
            66,
        ),  # don't consider seconds
    ],
)
def test_time_to_minutes(time, expected):
    assert round(time.seconds / 60) == expected

