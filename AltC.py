__author__ = 'rfischer'

T = input()
for i in range(0,T):
    min_deletions = 0
    s = raw_input()

    prev_j = 'z'
    for j in s:
        if j == prev_j:
            min_deletions += 1
        prev_j = j

    print min_deletions