from process_days_input import *
from process_output2 import *


def date_after(user_input):
    # raw date DELIMITER raw lapse
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INVALID_INPUT
    try:
        return process_date_ouput(date + lapse, False)
    except OverflowError:
        return INVALID_INPUT


def date_before(user_input):
    # raw date DELIMITER raw lapse
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INVALID_INPUT
    try:
        return process_date_ouput(date - lapse, False)
    except OverflowError:
        return INVALID_INPUT


def days_between(user_input):
    # raw date DELIMITER raw date
    try:
        start, end = map(lambda u: u.replace(hour=0, minute=0, second=0, microsecond=0), process_datedate(user_input))
    except AttributeError:
        return INVALID_INPUT
    try:
        return process_date_ouput(abs(end - start), True)
    except OverflowError:
        return INVALID_INPUT


def get_day_of_week(user_input):
    # raw date
    date = process_date(user_input)
    try:
        return date.strftime('%A')
    except AttributeError:
        return INVALID_INPUT


def get_today():
    return process_date_ouput(datetime.datetime.now(tz=MOSCOW), delta=False)


def how_many(user_input):
    # raw date DELIMITER raw date DELIMITER day of week
    # or
    # raw date DELIMITER day of week
    start, end, week_day = process_datedateday(user_input)
    if not (start and end and week_day) or start >= end:
        return INVALID_INPUT
    lapse = (end - start).days
    res = lapse // 7
    remainder = lapse % 7
    remaining_date = end - datetime.timedelta(remainder)
    while remaining_date <= end:
        if remaining_date.strftime('%a') == week_day:
            res += 1
            break
        remaining_date += datetime.timedelta(1)
    return res




