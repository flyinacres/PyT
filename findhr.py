__author__ = 'rfischer'
import re

T = input()

p1 = re.compile('^hackerrank')
p2 = re.compile('.*hackerrank$')
for t in range(0, T):

    _s = raw_input()
    m = p1.match(_s)
    m2 = p2.match(_s)
    if m and m2:
        print "0"
    elif m:
        print 1
    elif m2:
        print 2
    else:
        print "-1"