import datetime
import time
gigasecond = 1000000000
bday = datetime.date(1978,5,12)
print(f"birthday : {bday}")
days_since_birth = datetime.date.today() - bday
days_since_birth_in_seconds = days_since_birth.days * 86400
delta = gigasecond - days_since_birth_in_seconds
if delta == gigasecond:
    print(f"the gigasecond anniversary is today : {datetime.date.today()}")
elif delta > 0:
    seconds = days_since_birth_in_seconds + delta
    #gigasecond_bday = datetime.timedelta(seconds=seconds)
    gigasecond_bday = datetime.date.fromtimestamp(seconds)
    print(f"the gigasecond anniversary is : {gigasecond_bday}")
else:
    seconds = days_since_birth_in_seconds - delta
    gigasecond_bday = datetime.date.fromtimestamp(seconds)
    print(f"the gigasecond anniversary is : {gigasecond_bday}")      
