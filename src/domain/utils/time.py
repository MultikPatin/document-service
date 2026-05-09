from datetime import UTC, datetime, tzinfo


def time_now(tz: tzinfo = UTC) -> datetime:
    return datetime.now(tz)
