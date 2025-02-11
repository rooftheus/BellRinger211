import datetime

pst = datetime.tz.gettz('America/Los_Angeles')

now = datetime.datetime.now()
feb_14 = datetime.datetime(2025, 2, 14, 12)

print(feb_14.astimezone(pst) - now.astimezone(pst))



