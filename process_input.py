from datetime import datetime, timedelta
from global_vars import *


def process_date(raw_date, loc):
    now = datetime.utcnow()
    if raw_date == 'now':
        return now
    order = [DAY, MONTH, YEAR]
    dict_date = dict(zip(order, map(int, raw_date.split(DOT))))
    date = datetime(**{key: dict_date.get(key, getattr(now, key)) for key in order})
    return loc.localize(date, is_dst=None).astimezone(UTC)


def process_lapse(raw_lapse, daywise):
    if daywise:
        return timedelta(days=int(raw_lapse))
    order = [SECONDS, MINUTES, HOURS, DAYS, WEEKS]
    return timedelta(**{key: dict(zip(order, map(int, reversed(raw_lapse.split(COLON))))).get(key, 0) for key in order})


if __name__ == '__main__':
    print(process_date('now', MOSCOW))
    # print(process_lapse("50", True))

