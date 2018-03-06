from process_input import *
from process_output import *


def find_day_after(user_input, loc=None):
    answer = "{date} + {lapse} days = {result}"
    if not loc:
        loc = MOSCOW
    try:
        raw_date, raw_lapse = map(lambda d: d.strip(), user_input.split(DELIMITER))
        date = str_to_date(raw_date, loc)
        lapse = str_to_lapse(raw_lapse, daywise=True)
    except ValueError as e:
        return e
    return answer.format(date=date_to_str(date, loc, with_dow=False),
                         lapse=lapse_to_days(lapse),
                         result=date_to_str(date + lapse, loc, with_dow=False))




if __name__ == '__main__':
    pass
    print(find_day_after('now / 5'))
