#!/usr/bin/env python

from datetime import datetime, timedelta
from astral import Astral, Location
import time, sys, pytz
from sh import ddcctl
from tzlocal import get_localzone

####### CONFIGURATION STARTS HERE #######

LAT = 43.5321
LNG = 3.8618

BRIGHTNESS_1 = 0
BRIGHTNESS_2 = 10
BRIGHTNESS_3 = 20

####### CONFIGURATION STOPS HERE #######


d = datetime.now(pytz.timezone("UTC"))
location = Location(('local', 'europe', LAT, LNG, 'UTC'))

def get_level(sun, d):
    def t(d):
        return time.mktime(d.timetuple())

    def a(v1, v2, v3):
        return int(v2 + v1*(v3-v2))

    if d < sun['dawn']:
        return BRIGHTNESS_1
    elif d < sun['sunrise']:
        v = (t(d)-t(sun['dawn'])) / (t(sun['sunrise'])-t(sun['dawn']))
        return a(v, BRIGHTNESS_1, BRIGHTNESS_2)
    elif d < sun['noon']:
        v = (t(d)-t(sun['sunrise'])) / (t(sun['noon'])-t(sun['sunrise']))
        return a(v, BRIGHTNESS_2, BRIGHTNESS_3)
    elif d < sun['sunset']:
        v = (t(sun['sunset']) - t(d)) / (t(sun['sunset'])-t(sun['noon']))
        return a(v, BRIGHTNESS_2, BRIGHTNESS_3)
    elif d < sun['dusk']:
        v = (t(sun['dusk'])-t(d)) / (t(sun['dusk'])-t(sun['sunset']))
        return a(v, BRIGHTNESS_1, BRIGHTNESS_2)
    else:
        return BRIGHTNESS_1

brightness = get_level(location.sun(), d)

if False:
    for i in range(1440):
        d2 = d.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(minutes=i)
        print("%s %s" % (d2, get_level(location.sun(), d2)))


if True:
    print("Today times: (%s)" % get_localzone())
    for t in ('dawn', 'sunrise', 'noon', 'sunset', 'dusk'):
        title = (t.title()+":").ljust(9)
        local_time = location.sun()[t].astimezone(get_localzone()).strftime('%H:%M')
        print("  %s%s" % (title, local_time))

print("")

#./ddcctl -d 1 -b 20
print("Setting brightness to: %s" % brightness)
ret = ddcctl("-d", 1, "-b", brightness)
print(ret)
