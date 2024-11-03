from datetime import datetime


def convert_epoch_to_datetime(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')