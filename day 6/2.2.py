"""
Write a recursive function that prompt the user for a string of characters, strip out 
the spaces and punctuation signs, lowercase the string, then test if is a palindrome.

It should return ”True” for "never odd or even" and "A Santa Lived As a Devil at NASA."

"""




ponctuation = (",",";",":","!","?",".",'"',"'")
mot = input("ecrivez quelque chose:")
mot = mot.replace(" ", "").strip().lower() # evite de faire la ligne 15 et 16 donc permet de gagner du temps
# mot = mot.strip()
# mot = mot.lower()
for i in ponctuation:
    mot = mot.replace(i , "")

print(mot)

# mot = "kayak"
def palidrome(mot):
    if mot == "": #permet de sortir de ma recurssive
        return bool(True) 
    elif mot[0]== mot[-1]:
        return palidrome(mot[1:-1]) #rapel de la fonction donc recurssion 
    else:
        return bool(False) #une fonction doit toujours donner un resultat d'ou le return
      

result = palidrome(mot)
print(result)




# j'aurai pu faire ca directement sans passer par une recursive mot2 = mot[::-1]


