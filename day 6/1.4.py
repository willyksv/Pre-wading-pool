"""
https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3-fr
Write a function that:
✓ takes the number of sandwiches to prepare as a parameter ;
✓ then displays as many sandwiches as requested.

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

number = 0

while number <= 0:
    number_str = (input("combien ?"))
    try: # permet de tester si il y a une erreur
        number = int(number_str) 
    except:
        print("I can't do this !")
        number = 0
        continue #permet de passer la boucle et la faire repeter voir aussi la commande break sur internet
    if number > 0:
        for nombre_de_sandwich in range(number):
            print("\r") #permet de faire un saut de ligne 
            sandwich()
    else:
        print("I can't do this !")
