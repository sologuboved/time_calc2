from operator import add, sub
from conversions import *


def find_time(user_input, loc=None):
    if not loc:
        loc = MOSCOW
    try:
        raw_start, raw_lapse = user_input.split(DELIMITER)
        start = join_datetimelet(raw_start.strip(), loc)
        print(start)
        lapse = str_to_lapse(raw_lapse.strip(), daywise=False)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    find_time("now 10:1 / 20:0")

