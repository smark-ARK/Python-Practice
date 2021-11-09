inSec = int(input('Duration in Seconds: '))
secperday = 24*60*60
secperhour = 60*60
secspermin = 60

days = inSec/secperday
print(inSec)
inSec %= secperday
print(inSec)

hours = inSec/secperhour
inSec = inSec % secperhour

mins = inSec/secspermin
inSec = inSec % secspermin

secs = inSec

print('The duration is: ', '%d:%02d:%02d:%02d' %
      (days, hours, mins, secs))
