from conversions import convert


def date_to_str(date, loc, with_dow):
    formatter = "%d %B %Y"
    if with_dow:
        formatter += ", %A"
    return convert(date, loc, to_utc=False).strftime(formatter)


def lapse_to_days(lapse):
    return lapse.days
