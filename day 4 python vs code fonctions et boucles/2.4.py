"""
For all integers from -30 to 30:
✓ if it's a multiple of 3, display ”Fizz” ;
✓ if it's a multiple of 5, display ”Buzz” ;
✓ if it's a multiple of 3 and 5, display ”FizzBuzz” ;
✓ if it does not meet any of the previous conditions, just print the integer itself.
"""

nombre = int(input("taper un nombre entier:"))
if nombre % 3 == 0 and nombre % 5 == 0 and nombre >= -30 and nombre <= 30:
    print("fizzbuzz")
elif nombre % 3 == 0 and nombre >= -30 and nombre <= 30:
    print("fizz")
elif nombre % 5 == 0 and nombre >= -30 and nombre <= 30:
    print("buzz")
else:
    print(nombre)

# attention a l'ordre des conditions
