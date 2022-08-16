import datetime


def current_date(request):
    request['date'] = datetime.date.today()
