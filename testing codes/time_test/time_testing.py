import datetime

now = datetime.datetime.now()

today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)

now2 = datetime.datetime.now()

print(now2 > today8am)
