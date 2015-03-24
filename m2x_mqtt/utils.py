import time

from datetime import date, datetime
from json import JSONEncoder

from iso8601 import iso8601


class DateTimeJSONEncoder(JSONEncoder):
    def default(self, value):
        if isinstance(value, (datetime, date)):
            return to_iso(value)
        else:
            return super(DateTimeJSONEncoder, self).default(value)


def to_utc(dtime):
    timestamp = time.mktime(dtime.timetuple())
    dtime_utc = datetime.utcfromtimestamp(timestamp)
    dtime_utc = dtime_utc.replace(tzinfo=iso8601.UTC,
                                  microsecond=dtime.microsecond)
    return dtime_utc


def to_iso(dtime):
    if not isinstance(dtime, (date, datetime)):
        dtime = iso8601.parse_date(dtime)
    dtime = to_utc(dtime)
    return dtime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def tags_to_server(tags):
    if not isinstance(tags, (list, tuple)):
        tags = [tags]
    return ','.join(tags)


def from_server(name, value):
    if name == 'tags':
        if isinstance(value, str):
            value = value.split(',')
    else:
        try:
            value = iso8601.parse_date(value)
        except iso8601.ParseError:
            pass
    return value


def to_server(name, value):
    if name == 'tags':
        value = tags_to_server(value)
    elif isinstance(value, (datetime, date)):
        value = to_iso(value)
    return value


def attrs_from_server(attrs):
    return dict((name, from_server(name, value))
                    for name, value in attrs.items())


def attrs_to_server(attrs):
    return dict((name, to_server(name, value))
                    for name, value in attrs.items())
