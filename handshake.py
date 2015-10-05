#import math
T = input()

for i in range(0, T):
    n = input()
    if n > 1:
        print (n * (n-1))   / 2
        #print math.factorial(n)/(2*math.factorial((n-2)))
    else:
        print 0