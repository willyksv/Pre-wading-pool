"""
Make 4 of those lettuce-tomato-double ham sandwiches.
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

for number in range(4):
    print("\r") #permet de faire un saut de ligne 
    sandwich()
