__author__ = 'giasuddin'

import datetime

date_today = datetime.date.today()

previos_day= date_today - datetime.timedelta(days=1)

print(date_today)
print(previos_day)
