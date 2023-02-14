from datetime import datetime, time
def diff(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
dt1 = datetime.strptime('2003-12-15 16:30:00', '%Y-%m-%d %H:%M:%S')
dt2 = datetime.now()
print(f"My age in seconds {(diff(dt2, dt1))}")
