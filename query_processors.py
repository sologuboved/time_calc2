import traceback
import logging
from global_vars import DELIMITER
from conversions import str2date, str2datetimelet, str2delta, date2str, datetimelet2str, delta2days


def basic_processor(update, context, processor):
    query = update['message']['text']
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    try:
        text = processor(query)
    except Exception:
        traceback_msg = traceback.format_exc()
        logging.error(traceback_msg)
        text = "Wrong query"
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def daft(query):
    raw_date, raw_lapse = itemize(query)
    return date2str(add(str2date(raw_date), str2delta(raw_lapse, True)))


def dbef(query):
    raw_date, raw_lapse = itemize(query)
    return date2str(subtract(str2date(raw_date), str2delta(raw_lapse, True)))


def dbetw(query):
    raw_beg, raw_fin = itemize(query)
    return delta2days(subtract(*sorted((str2date(raw_fin), str2date(raw_beg)))))


def itemize(query):
    return map(str.strip, query.split(DELIMITER))


def add(item0, item1):
    return item0 + item1


def subtract(beg, fin):
    return fin - beg


if __name__ == '__main__':
    print(dbetw("5.3.2018 / 2.3.2018"))
