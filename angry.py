

T = input()

for i in range(0, T):
    N, K = [int(x) for x in raw_input().split(' ')]

    arrivals = [int(x) for x in raw_input().split(' ')]
    present = [1 for x in arrivals if x <= 0]
    #print "sum is " + str(sum(present))
    if sum(present) < K:
        print "YES"
    else:
        print "NO"