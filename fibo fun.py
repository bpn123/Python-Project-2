# Python program for Fibonacci numbers.

def recursion_fib(n):
   if n <= 1:
       return n
   else:
       return(recursion_fib(n-1) + recursion_fib(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci numbers are:")
   for i in range(nterms):
       print(recursion_fib(i))
