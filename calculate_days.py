from operator import add, sub
from process_input import *
from process_output import *


def find_date(user_input, plus, loc=None):
    answer = "{date} {sign} {lapse} days = {result}"
    if plus:
        operation = add
        sign = PLUS
    else:
        operation = sub
        sign = MINUS
    if not loc:
        loc = MOSCOW
    try:
        raw_date, raw_lapse = map(lambda d: d.strip(), user_input.split(DELIMITER))
        date = str_to_date(raw_date, loc)
        lapse = str_to_lapse(raw_lapse, daywise=True)
    except ValueError as e:
        return e
    return answer.format(sign=sign,
                         date=date_to_str(date, loc, with_dow=False),
                         lapse=lapse_to_days(lapse),
                         result=date_to_str(operation(date, lapse), loc, with_dow=False))


def find_days(user_input, loc=None):
    answer = "{fin} - {start} = {result} days"
    if not loc:
        loc = MOSCOW
    try:
        raw_start, raw_fin = map(lambda d: d.strip(), user_input.split(DELIMITER))
        start = str_to_date(raw_start, loc)
        fin = str_to_date(raw_fin, loc)
    except ValueError as e:
        return e
    start, fin = sorted([start, fin])
    return answer.format(start=date_to_str(start, loc, with_dow=False),
                         fin=date_to_str(fin, loc, with_dow=False),
                         result=lapse_to_days(fin - start))


if __name__ == '__main__':
    pass
    # print(find_date('now / 5', plus=False))
    print(find_days("10"))
