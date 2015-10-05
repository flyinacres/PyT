__author__ = 'rfischer'
import re

T = input()

p = re.compile('([0-9]{1,3})[ -]{1}([0-9]{1,3})[ -]{1}([0-9]{4,10})')
for t in range(0, T):
    _s = raw_input()
    m = p.match(_s)
    if m:
        print 'CountryCode=' + str(m.group(1)) + ',LocalAreaCode=' + str(m.group(2)) + ',Number=' + str(m.group(3))
    else:
        print "NO"
