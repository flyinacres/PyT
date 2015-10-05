__author__ = 'rfischer'

T = input()

s = raw_input()
a = set(s)
for i in range(1,T):
    min_deletions = 0
    s = raw_input()
    a = a.intersection(set(s))

print len(set(a))