"""
https://www.geeksforgeeks.org/dsa/sum-of-natural-numbers-using-recursion/

Write a recursive function that computes the sum of all integers from 1 to n, a given parameter

The parameter 42 should return 903.

"""

def integer_sum(n):
    if n ==0:
        return n #va stopper la fonction et nous donner une valeur 
    else:
       return n + integer_sum(n - 1)
print(integer_sum(42))




