def construct_day_title():
    date = [datetime.now().year, datetime.now().month, datetime.now().day]
    file_name = "-".join(str(e) for e in date) + '.md'
    return file_name


def construct_entry_timestamp():
    now = datetime.now()
    timestamp = [now.hour, now.minute]
    timestamp = [str(e) for e in timestamp]
    timestamp = ':'.join(timestamp)
    return timestamp
