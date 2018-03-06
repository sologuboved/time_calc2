from datetime import datetime, timedelta
from global_vars import *


def str_to_date(raw_date, loc):
    now = datetime.now(tz=loc)
    if raw_date == 'now':
        return now
    order = [DAY, MONTH, YEAR]
    date = {key: dict(zip(order, map(int, raw_date.split(DOT)))).get(key, getattr(now, key)) for key in order}
    if date[YEAR] < 100:
        date[YEAR] += 2000
    return convert_to_utc(datetime(**date), loc)


def str_to_lapse(raw_lapse, daywise):
    if daywise:
        return timedelta(days=int(raw_lapse))
    order = [SECONDS, MINUTES, HOURS, DAYS, WEEKS]
    return timedelta(**{key: dict(zip(order, map(int, reversed(raw_lapse.split(COLON))))).get(key, 0) for key in order})


def str_to_dow(raw_dow):
    if raw_dow not in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
        raise ValueError("{} is not day of week".format(raw_dow))
    return raw_dow


def convert_to_loc(date, loc):
    try:
        return UTC.localize(date, is_dst=None).astimezone(loc)
    except ValueError:
        return date.astimezone(loc)


def convert_to_utc(date, loc):
    return loc.localize(date, is_dst=None).astimezone(UTC)


if __name__ == '__main__':
    print(str_to_date('07', MOSCOW))
    # print(str_to_lapse("50", True))

