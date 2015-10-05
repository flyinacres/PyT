__author__ = 'rfischer'
import re

T = input()

p = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')
#p = re.compile('[a-z]{3}[0-9]{4}')
for t in range(0, T):
    _s = raw_input()
    if p.match(_s):
        print "YES"
    else:
        print "NO"
