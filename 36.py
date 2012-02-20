#!/usr/bin/python

def digits(n, base):
   while True:
      prevn = n
      n = n // base
      if prevn > 0:
         yield(prevn - (n * base))
      else:
         break

def ispalindrome(l):
   l = list(l)
   return l == list(reversed(l))

sum = 0
for i in range(1, 1000000):
   if ispalindrome(digits(i,10)) and ispalindrome(digits(i,2)):
      sum += i
      print(str(i) + " is palindromic in base 10 and 2.    Sum is "+str(sum))
      
