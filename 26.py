#!/usr/bin/python

# This uses long division. 'List' contains the number you would get after
# subtracting the highest multiple of n that is less than the last one (called
# q) in the tail if you were to do it on paper. If q has already been added to
# the list this means that there is a cycle, because the tail would repeat
# itself. The length is the same as the first occurrence of q up until the last
# number in the list.

def cyclelength(n):
   if n <= 1 or n % 1 != 0:
      raise Exception("Only integers over 1 are allowed.")
   list = [1]
   while True:
      q = list[-1] * 10 - list[-1] * 10 // n * n
      if q in list:
         return len(list) - list.index(q)
      else:
         list.append(q)

largest = 0
for i in range(2,1000):
   c = cyclelength(i)
   if c > largest:
      largest = c

print(largest)
