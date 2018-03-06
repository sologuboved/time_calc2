from process_hours_input import *
from process_output2 import *


def calculate_time_sequence(user_input):
    # raw timelet {+, -, *} raw timelet ...
    processed_series = process_time_sequence(user_input)
    if not processed_series:
        return INVALID_INPUT

    first_timelet = processed_series[0]
    curr_res = convert_to_secs(*first_timelet)

    ind = 1
    while ind + 1 < len(processed_series):
        sign = processed_series[ind]

        if sign == PLUS:
            curr_res += convert_to_secs(*processed_series[ind + 1])
        elif sign == MINUS:
            curr_res -= convert_to_secs(*processed_series[ind + 1])
        elif sign == ASTERIX:
            curr_res *= processed_series[ind + 1]
        ind += 2

    return process_time_output(convert_to_dhms(curr_res), with_date=False)


def time_after(user_input):
    # raw date raw timelet DELIMITER raw timelet
    date, initial_timelet, lapse = process_timelapse(user_input)
    if not (date and initial_timelet and lapse):
        return INVALID_INPUT

    hrs, mins, secs = initial_timelet
    date = date.replace(hour=hrs, minute=mins, second=secs)
    hrs, mins, secs = lapse
    delta = datetime.timedelta(hours=hrs, minutes=mins, seconds=secs)
    date += delta

    return process_time_output(date, with_date=True)


def time_before(user_input):
    # raw date raw timelet DELIMITER raw timelet
    date, initial_timelet, lapse = process_timelapse(user_input)
    if not (date and initial_timelet and lapse):
        return INVALID_INPUT

    hrs, mins, secs = initial_timelet
    date = date.replace(hour=hrs, minute=mins, second=secs)
    hrs, mins, secs = lapse
    delta = datetime.timedelta(hours=hrs, minutes=mins, seconds=secs)
    date -= delta

    return process_time_output(date, with_date=True)


def time_between(user_input):
    # raw date raw timelet DELIMITER raw date raw timelet
    start_date, start_time, end_date, end_time = process_timetime(user_input)
    if not (start_date and start_time and end_date and end_time):
        return INVALID_INPUT

    hrs, mins, secs = start_time
    start_date = start_date.replace(hour=hrs, minute=mins, second=secs)
    hrs, mins, secs = end_time
    end_date = end_date.replace(hour=hrs, minute=mins, second=secs)

    return str(abs(end_date - start_date))


def get_now():
    now = datetime.datetime.now(tz=MOSCOW)
    return process_time_output((now.hour, now.minute, now.second), with_date=False)
