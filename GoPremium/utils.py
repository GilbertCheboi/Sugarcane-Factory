from datetime import datetime

def convert_timestamp():
    unformatime_timestamp = datetime.now()

    formated_timestamp = unformatime_timestamp.strftime("%Y%m%d%H%M%S")

    return formated_timestamp