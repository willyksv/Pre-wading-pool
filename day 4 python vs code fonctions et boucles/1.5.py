"""if it's 42, display ”a” ;
✓ if it's smaller or equal than 21, display ”b” ;
✓ if it's even, display ”c” ;
✓ if this integer divided by 2 is smaller than 21 (excluded), display ”d” ;
✓ finally, if it's is odd and greater or equal than 45, display ”e” ;
✓ in any other cases, display ”f”."""

a = int(input("ecrivez un nombre entier:"))
if a == 42:
    print("a") 
elif a <= 21:
    print("b")
elif a %2 == 0:
    print("c")
elif (a /2)< 21: 
    print("d")
elif a %2 == 0 and a >= 45:
    print("e")
else:
    print("f")