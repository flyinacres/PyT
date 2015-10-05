__author__ = 'rfischer'

s = raw_input()
a = set(s)

t = raw_input()
b = set(t)

del_count = 0

# first count all the chars not in both
c = a.symmetric_difference(b)
for d in c:
    del_count += s.count(d)
    del_count += t.count(d)

# now count where char is in both, but different number of times
c = a.intersection(b)
for d in c:
    cs = s.count(d)
    ct = t.count(d)
    if cs > ct:
        del_count += cs - ct
    else:
        del_count += ct - cs

print del_count