
n,a,b = [int(x) for x in raw_input().split(' ')]
d = [int(x) for x in raw_input().split(' ')]

z = 1
weights = [n-1] * n
e = n / 2 + n % 2
for i in range(1, e):
    z *= 2
    for j in range(i, n-i):
        weights[j] += (n - z)

#print weights
print sum([x*y for x,y in zip(d, weights)])/float(n)
