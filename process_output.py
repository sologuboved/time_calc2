from global_vars import UTC


def date_to_str(date, loc, with_dow):
    formatter = "%d %B %Y"
    if with_dow:
        formatter += ", %A"
    local_date = UTC.localize(date, is_dst=None).astimezone(loc)
    print(local_date)
    return local_date.strftime(formatter)


def lapse_to_days(lapse):
    return lapse.days
