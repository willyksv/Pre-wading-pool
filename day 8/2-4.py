"""
Using turtle, write a program to draw a spiral.
utiliser les math, une spiral est un demi cercle qui s'agrandit 
https://zestedesavoir.com/tutoriels/944/a-la-decouverte-de-turtle/tracer-et-dessiner/

"""
import turtle

turtle.shape ('turtle') #affiche le curseur en forme de tortue

a = 1   #StartingAngle

for i in range (20): #nombre de demi cercle
    turtle.circle(a,180) 
    a = a + 20 #aggrandit le demi cercle

turtle.done()