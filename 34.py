#!/usr/bin/python

# What a lame problem. It only generated two numbers in under a minute and
# their sum turned out to be the answer. 

def fact(n):
   if n > 0:
      return n * fact(n-1)
   else:
      return 1

def digits(n):
   while True:
      prevn = n
      n = n // 10
      if prevn > 0:
         yield(prevn - (n * 10))
      else:
         break

def iscurious(n):
   sum = 0
   for i in digits(n):
      sum += fact(i)
   return sum == n

sum = 0
i = 3
print(0)
while True:
   if iscurious(i):
      sum += i
      print("+ "+ str(i)+" = " + str(sum))
   i += 1
