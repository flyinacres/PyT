import math
f = 0.70710678118654752440084436210485

# Need a change in order to get this committed to git
L, S1, S2 = [int(x) for x in raw_input().split(' ')]
N = input()

S1, S2 = (S1, S2) if S1 < S2 else (S2, S1)

for i in range(0, N):
    q = input()
    r = (math.sqrt(q) - L) / (f * (S1 - S2))
    print r
    if r == 0:
        print "%.5f" % 0.00000
    else:
        print "%.5f" % r
