from datetime import datetime, timedelta
from global_vars import *


def str_to_date(raw_date, loc):
    now = datetime.now(tz=loc)
    if raw_date == NOW:
        return convert(now, loc, to_utc=True)
    order = [DAY, MONTH, YEAR]
    date = {key: dict(zip(order, map(int, raw_date.split(DOT)))).get(key, getattr(now, key)) for key in order}
    if date[YEAR] < 100:
        date[YEAR] += 2000
    return convert(datetime(**date), loc, to_utc=True)


def str_to_lapse(raw_lapse, daywise):
    if daywise:
        return timedelta(days=int(raw_lapse))
    order = [SECONDS, MINUTES, HOURS, DAYS, WEEKS]
    return timedelta(**{key: dict(zip(order, map(int, reversed(raw_lapse.split(COLON))))).get(key, 0) for key in order})


def str_to_dow(raw_dow):
    if raw_dow not in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
        raise ValueError("{} is not day of week".format(raw_dow))
    return raw_dow


def join_datetimelet(raw_datetimelet, loc):
    now = datetime.now(tz=loc)
    if raw_datetimelet == NOW:
        return convert(now, loc, to_utc=True)
    raw_date, raw_timelet = raw_datetimelet.split()
    date_order = [DAY, MONTH, YEAR]
    if raw_date == NOW:
        dict_date = dict()
    else:
        dict_date = dict(zip(date_order, map(int, raw_date.split(DOT))))
    date = {key: dict_date.get(key, getattr(now, key)) for key in date_order}
    if date[YEAR] < 100:
        date[YEAR] += 2000
    time_order = [HOUR, MINUTE, SECOND]
    timelet = {key: dict(zip(time_order, map(int, raw_timelet.split(COLON)))).get(key, 0) for key in time_order}
    datetimelet = {**date, **timelet}
    return convert(datetime(**datetimelet), loc, to_utc=True)


def date_to_str(date, loc, with_dow):
    formatter = "%d %B %Y"
    if with_dow:
        formatter += ", %A"
    return convert(date, loc, to_utc=False).strftime(formatter)


def lapse_to_days(lapse):
    return lapse.days


def convert(date, loc, to_utc):
    if to_utc:
        source, target = loc, UTC
    else:
        source, target = UTC, loc
    try:
        return source.localize(date, is_dst=None).astimezone(target)
    except ValueError:
        return date.astimezone(target)


if __name__ == '__main__':
    print(str_to_date('now', MOSCOW))
    # print(str_to_lapse("50", True))

