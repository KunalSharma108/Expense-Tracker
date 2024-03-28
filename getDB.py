import datetime
import Nametime

def getDate():
    full_date = datetime.datetime.now()
    year = full_date.year
    month = full_date.month
    day = full_date.day

    month = Nametime.nameMonth(month)
    tb_name = f"{day}_{month}_{year}"

    return tb_name