import datetime
date = datetime.datetime.now().date()
time = datetime.datetime.now().time().replace(microsecond=0)
print('Today is', (date), 'and it is', (time))
