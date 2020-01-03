import datetime


def get_year_month_day(raw_date):
    today = datetime.datetime.today()
    date = raw_date.split('.')
    month, year = today.month, today.year
    if len(date) == 3:
        day, month, year = date
    elif len(date) == 2:
        day, month = date
    elif len(date) == 1:
        day = date[0]
    else:
        raise ValueError("Unsuitable string")
    return [int(item) for item in (year, month, day)]


def get_hour_minute_second(raw_timelet):
    timelet = raw_timelet.split(':')
    hour = minute = 0
    if len(timelet) == 3:
        hour, minute, second = timelet
    elif len(timelet) == 2:
        minute, second = timelet
    elif len(timelet) == 1:
        second = timelet[0]
    else:
        raise ValueError("Unsuitable string")
    return [int(item) for item in (hour, minute, second)]


def str2date(raw_date):
    raw_date = raw_date.strip()
    today = datetime.datetime.today()
    if raw_date == 'today':
        return today
    return datetime.datetime(*get_year_month_day(raw_date))


def str2datetimelet(raw_datetimelet):
    raw_datetimelet = raw_datetimelet.strip()
    if raw_datetimelet == 'now':
        return datetime.datetime.now()
    raw_date, raw_timelet = map(str.strip, raw_datetimelet.split())
    year, month, day = get_year_month_day(raw_date)
    hour, minute, second = get_hour_minute_second(raw_timelet)
    return datetime.datetime(year, month, day, hour, minute, second)


def str2delta(raw_delta):
    raw_delta = raw_delta.strip()
    hour, minute, second = get_hour_minute_second(raw_delta)
    return datetime.timedelta(seconds=second, minutes=minute, hours=hour)


def date2str(date):
    return '{0:%d.%m.%Y}'.format(date)


def datetimelet2str(datetimelet):
    return '{0:%d.%m.%Y %H:%M:%S}'.format(datetimelet)
