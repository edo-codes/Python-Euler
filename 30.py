#!/usr/bin/python

# Again, cheating. See problem 34.

def digits(n):
   while True:
      prevn = n
      n = n // 10
      if prevn > 0:
         yield(prevn - (n * 10))
      else:
         break

def issurprising(n):
   sum = 0
   for i in digits(n):
      sum += i**5
   return n == sum

# I don't understand why this doesn't work.
#def issurprising(n):
#   return n == sum(x**5 for x in digits(n))

sum = 0
for i in range(2, 100000000):
   if issurprising(i):
      sum += i
      print("+ "+ str(i)+ " = "+str(sum))
