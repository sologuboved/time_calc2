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


def find_dow(user_input, loc=None):
    if not loc:
        loc = MOSCOW
    try:
        date = str_to_date(user_input, loc)
    except ValueError as e:
        return e
    return date_to_str(date, loc, with_dow=True)


def find_how_many(user_input, loc=None):
    answer = "Between {start} and {fin}, there {predicate} {res} {dow}{inflection}"
    if not loc:
        loc = MOSCOW
    try:
        raw_start, raw_fin, raw_dow = map(lambda d: d.strip(), user_input.split(DELIMITER))
        start = str_to_date(raw_start, loc)
        fin = str_to_date(raw_fin, loc)
        dow = str_to_dow(raw_dow)
    except ValueError as e:
        return e
    start, fin = sorted([start, fin])
    print(start)
    print(fin)
    lapse = (fin - start).days
    res = lapse // 7
    remainder = lapse % 7
    remaining_date = fin - timedelta(remainder)
    print(remaining_date)
    while remaining_date <= fin:
        if remaining_date.strftime('%a') == dow:
            res += 1
            break
        remaining_date += timedelta(1)
    if res == 1:
        predicate = 'is'
        inflection = ''
    else:
        predicate = 'are'
        inflection = 's'
    return answer.format(start=date_to_str(start, loc, with_dow=False),
                         fin=date_to_str(fin, loc, with_dow=False),
                         predicate=predicate, res=res, dow=dow, inflection=inflection)




if __name__ == '__main__':
    pass
    # print(find_date('now / 5', plus=False))
    # print(find_days("10.3.19 / 20.3.19"))
    # print(find_dow('07.03.18'))
    print(find_how_many("7 / 19 / Mon"))

