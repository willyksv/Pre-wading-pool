"""
Write a little program that computes the power function as fast as possible.
How long does your program takes to compute 42^84? and 42^168?
Compare your times and your code with your neighbors.

You are not allowed to use the system function (ca veux dire ne pas utiliser le**)
"""

import time
start = time.time() #sert a chronometrer
number = 42
power = 84

result = number
power2 = 1
while power2 < power:
    result = result * number
    power2 += 1
print(result) #si je ne print pas le result je  peux diminuer le temps

print(f"Time taken: {time.time() - start}") #sert a chronometrer