__author__ = 'rfischer'
import re

T = input()

p = re.compile('\([+-]?([1-9][0-9]{0,1})(\.[0-9]+)?\,\ [+-]?([1-9][0-9]{0,2})(\.[0-9]+)?\)')
#p = re.compile('\([+-]?([0-9]{2})')
for t in range(0, T):
    _s = raw_input()
    m = p.match(_s)
    if m:
        s1 = m.group(1) if not m.group(2) else m.group(1) + m.group(2)
        s2 = m.group(3) if not m.group(4) else m.group(3) + m.group(4)
        if float(s1) <= 90.0 and float(s2) <= 180.0:
            print "Valid"
        else:
            print "Invalid"
    else:
        print "Invalid"