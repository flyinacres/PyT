__author__ = 'rfischer'

def findChar(s, offset, i, n):
    ts = ''
    for j in range(0,n):
        ts += s[i:i+j+1]
        if len(ts) >= offset:
            return ts[offset-1]

    return ''


def sizeOfStringsForChar():
    return 0


T = input()

for t in range(0, T):
    s = raw_input()
    K = input()

    # sorted unique chars
    suc = sorted(list(set(s)))
    sr = s[::-1]

    total_len = 0
    for c in suc:
        # get the count of c in string
        # for each occurrence, get the index, from back to front (smaller strings)
        # calculating the total length of the substrings for this instance of the char
        # Seems like python sorts lists of strings properly :)
        count = s.count(c)
        delta = 0
        i = 0
        for j in range(0, count):
            # searching the reversed string, so index will actually indicate number of chars before the end of string
            i = sr.find(c, i) + 1
            #TODO: Getting closer, but does not handle 'acac' where the 'a' and 'ac' should be counted once
            # it may be necessary to create a set to hold the unique values--this could get big
            delta += (i * (i + 1)) / 2

        if K <= total_len + delta:
            print findChar(s, K - total_len, i, n)
            break

        total_len += delta
