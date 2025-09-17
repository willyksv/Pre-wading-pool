"speed 0 faire la forme en instantané"

import turtle

turtle.shape ('turtle') #affiche le curseur en forme de tortue

a = 1   #StartingAngle

for i in range (20): #nombre de demi cercle
    turtle.circle(a,180) 
    a = a + 20 #aggrandit le demi cercle

turtle.done()
