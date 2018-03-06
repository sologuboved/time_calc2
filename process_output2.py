import datetime


def process_date_ouput(output, delta):
    if delta:
        output = output.days
        if output == 1:
            inflection = ''
        else:
            inflection = 's'
        return "%d day%s" % (output, inflection)

    return output.strftime("%d %B %Y, %A")


def process_time_output(output, with_date):
    if with_date:
        return output.strftime("%d %B %Y, %A %H:%M:%S")

    hrs, mins, secs = output
    return str(datetime.timedelta(hours=hrs, minutes=mins, seconds=secs))
