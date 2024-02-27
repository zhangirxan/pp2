import datetime

a = datetime.datetime(2020, 5, 15, 5, 10, 20)
b = datetime.datetime.now()

difference_in_minutes = (b - a).total_seconds() / 60
print(int(difference_in_minutes))