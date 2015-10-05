__author__ = 'rfischer'

def allStringsStartingWith(c):
    string_set = set()
    i = 0
    while i > -1:
        i = _s.find(c, i)
        if i > -1:
            for j in range(i, len(_s)):
                string_set.add(_s[i:j+1])
            # iff an occurrence was found, skip it next time
            i += 1
    return string_set

T = input()

for t in range(0, T):
    _s = raw_input()
    K = input()

    # sorted unique chars
    suc = sorted(list(set(_s)))

    total_len = 0
    found_char = ''
    string_part = ''
    for c in suc:
        # Get all strings beginning with c
        # Add them to a set to keep them unique
        string_part = "".join(sorted(list(allStringsStartingWith(c))))
        if (K - 1) < total_len + len(string_part):
            found_char = string_part[(K-1)-total_len]
            break
        total_len += len(string_part)


    #print string_part
    print found_char
