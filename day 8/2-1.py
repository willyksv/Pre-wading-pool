"""
Find the turtle package.
Then, install it on your machine.
Eventually, write a program that use this package to draw a square.

explication complementaires:
il est preferable de creer un environnement virtuel ".venv" quand on travail avec de package" il permet d'eviter de tout installer 
sur le pc et permet de dissocier les package quand on l'exporte 
https://pypi.org/project/PythonTurtle/
https://www.geeksforgeeks.org/python/draw-square-and-rectangle-in-turtle-python/
"""

import turtle 


#premiere solution:
t = turtle.Turtle()
s = int(input("Enter the length of the side of the Square:"))

# drawing first side
t.forward(s) 
t.left(90) 

# drawing second side
t.forward(s) 
t.left(90) 

# drawing third side
t.forward(s) 
t.left(90) 

# drawing fourth side
t.forward(s) 
t.left(90) 

turtle.done() # permet de figer le dessin a la fin

#seconde solution:

# import turtle
# t = turtle.Turtle()
# s = int(input("Enter the length of the side of square2:"))
# for _ in range(4):
#   t.forward(s) 
#   t.left(90) 