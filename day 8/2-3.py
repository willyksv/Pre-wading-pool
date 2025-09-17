"""
Using turtle, write a function draw_polygon(sides) that takes an integer parameter sides.
The function draws a regular polygon with the given number of sides:
✓ if sides = 3, then it draws an equilateral triangle ;
✓ if sides = 4, then it draws a square ;
✓ if sides = 5, then it draws a pentagon ;
✓ if sides = 6, then it draws a hexagon ;
✓ and so on...

"""
import turtle
t = turtle.Turtle()
s = int(input("entrer la longueur des traits:"))
cote = int(input("entrer le nombre de cotés:"))
angle = 360 / cote
for trait in range(cote):
  t.forward(s) 
  t.left(angle) 
turtle.done()