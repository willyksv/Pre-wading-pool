"""
Add a parameter to provide the possibility for veg sandwich (double vegetables + no ham).
If this option isn't specified, the sandwich must be a lettuce-tomato-double ham one by default.
"""

def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print (" O O O O O O ")
def ham () :
    print (" ============ ")

def sandwich():
    bread()
    lettuce()
    tomato ()
    ham()
    ham()
    bread()

def vegie_sandwich ():
    bread()
    lettuce()
    lettuce()
    tomato ()
    tomato () 
    bread()

number = 0

while number <= 0:
    number_str = (input("combien ?"))
    vegetarien = (input("ecris un truc si tu es vegetarien:" ))
    try: # permet de tester si il y a une erreur
        number = int(number_str) 
    except:
        print("I can't do this !")
        continue #permet de passer au reste de la boucle et de repeter la boucle  
    if number > 0 and vegetarien == "":
        for nombre_de_sandwich in range(number):
            print("\r") #permet de faire un saut de ligne 
            sandwich()
    elif number > 0 and not vegetarien == "":
        for nombre_de_sandwich in range(number):
            print("\r") #permet de faire un saut de ligne 
            vegie_sandwich()

    else:
        print("I can't do this !")
