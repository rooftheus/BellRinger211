import datetime
# import dateutil

# pst = dateutil.tz.gettz('America/Los_Angeles')

now = datetime.datetime.now()
feb_14 = datetime.datetime(2025, 2, 14, 0)

c = feb_14 - now

print(c.total_seconds() / 60 / 60)



