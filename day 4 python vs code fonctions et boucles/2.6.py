division = 2
nombre = int(input("taper un nombre entier:"))
# nombre = 14
nombre2 = nombre // division
division = division - 1
while division < nombre2:
    division = division + 1
    print()
    for multiple in range(nombre):
        if multiple % division == 0 and multiple > 0:
            print(multiple, end=" ")
