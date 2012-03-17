#!/usr/bin/python

d = "0"
for i in range(1, 1000000):
   d += str(i)

a = 0
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
   a = a * int(d[i])
   print(d[i])

print()
print(a)
