def fib(highest):
   x = 1
   y = 1
   z = 1
   while z <= highest:
      yield z
      z = x + y
      x = y
      y = z

def evenfib(highest):
   for i in fib(highest):
      if i % 2 == 0:
         yield i

print(sum(evenfib(4000000)))
