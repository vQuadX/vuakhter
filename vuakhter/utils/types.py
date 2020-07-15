from __future__ import annotations
import datetime
import typing

from vuakhter.utils.helpers import timestamp

DateOrDatetime = typing.Union[datetime.date, datetime.datetime]


class TimestampRange(typing.NamedTuple):
    start_ts: typing.Optional[int] = None
    end_ts: typing.Optional[int] = None

    @classmethod
    def from_datetime(
        cls, start_date: DateOrDatetime = None, end_date: DateOrDatetime = None, ms: bool = False,
    ) -> TimestampRange:
        start_ts = timestamp(start_date, ms=ms) if start_date else None
        end_ts = timestamp(end_date, ms=ms) if end_date else None

        return cls(start_ts, end_ts)

    def overlaps(self, other: TimestampRange, strict: bool = False) -> bool:
        if not (self.start_ts and self.end_ts and other.start_ts and other.end_ts):
            return not strict
        if self.end_ts <= other.start_ts or self.start_ts >= other.end_ts:
            return False
        return True


class AccessEntry(typing.NamedTuple):
    ts: int
    url: str
    method: str
    status_code: int
    request_id: str
    response_time: float


class RequestEntry(typing.NamedTuple):
    ts: int
    json: str
    request_id: str
    status_code: int


IndicesBoundaries = typing.Dict[str, TimestampRange]

AccessEntryIterator = typing.Iterator[AccessEntry]

RequestEntryIterator = typing.Iterator[RequestEntry]

AnyIterator = typing.Iterator[typing.Any]
