"""
https://pypi.org/project/english-words/1.1.0/
https://pypi.org/project/english-words/
https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
"""

hp = 11 
if hp >= 12:
    print("loose")

import random
import english_words

from english_words import(get_english_words_set)
web2lowerset = get_english_words_set(['web2'], lower=True)
word = random.choice(list(web2lowerset))
number_of_character = len(str(word))
print(word)
print(number_of_character)

def number_to_guess(word):
    hidden = ""
    for character in range(number_of_character - 1): #juste par soucis de presentation pour pouvoir ajouter le "_."
        hidden = "_ " + hidden
    hidden = hidden + "_."
    return hidden #vu que c'est une variable locale elle existe uniquement dans ma fonction number_to_guess donc j'utilise un return pour la faire sortir

hidden = number_to_guess(word)
print(hidden)
# print(number_to_guess(word))