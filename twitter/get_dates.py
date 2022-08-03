import datetime


def get_dates(days_before):
    return str(datetime.date.today()-datetime.timedelta(days=days_before)), str(datetime.date.today())
