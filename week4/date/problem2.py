import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

print(yesterday, yesterday.strftime("%A"))
print(today, today.strftime("%A"))
print(tomorrow, tomorrow.strftime("%A"))