__author__ = 'rfischer'
import re

T = input()

_total_tweets = 0
for t in range(0, T):
    _s = raw_input()
    if _s.lower().find("hackerrank") > -1:
        _total_tweets += 1

print _total_tweets
