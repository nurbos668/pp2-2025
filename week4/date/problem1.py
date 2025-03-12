import datetime

now = datetime.datetime.now()
five_days_ago = now - datetime.timedelta(days=5)

print(now, five_days_ago)