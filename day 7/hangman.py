"""
https://pypi.org/project/english-words/1.1.0/
https://pypi.org/project/english-words/
https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
https://www.geeksforgeeks.org/python/python-replace-to-k-at-ith-index-in-string/
"""

import random
import english_words

from english_words import(get_english_words_set)
web2lowerset = get_english_words_set(['web2'], lower=True)
word = random.choice(list(web2lowerset))
number_of_character = len(str(word))
print(word)
# print(number_of_character)

hp=12 
win=0
# print(hp)
def loose(hp):
    if hp < 1:
        print("game over")
        

def number_to_guess(word):
    hidden = ""
    for character in range(number_of_character - 1): #juste par soucis de presentation pour pouvoir ajouter le "_."
        hidden = "_ " + hidden
    hidden = hidden + "_." #au moment de sortir de la boucle
    return hidden #vu que c'est une variable locale elle existe uniquement dans ma fonction number_to_guess donc j'utilise un return pour la faire sortir
hidden = number_to_guess(word)
print(hidden,"     ","hp",hp)

def trouve_index():
    index = -1
    idx = []
    for i in word:
        if i == letter:
            index = word.find(letter,index+1)
            idx.append(int(index *2))
    return idx


def replace_blank(hidden):
    for i in range(len(hidden)):
        i = (i)
        n=0
        for i in idx:
            if i == idx[n]:
                i = int(i)
                n += 1
                hidden = hidden[:i]+ letter + hidden[i+1:]            
        else:
            hidden
    return hidden


while win ==0:
# letter= "a"
    guess = input("enter a letter or a word:")
    if len(guess) == 1:
        letter = guess
        idx = trouve_index()
        # print(idx)
        if idx == []:
            print("no")
            hp = hp -1
            # print(hp)
            loose(hp)
            if hp < 1:
                break
        hidden = replace_blank(hidden)
        print(hidden,"     ","hp:",hp)
        if "_" not in hidden:
            win = 1
            print("you win")
    else: 
        if guess == word:
            win = 1
            print("you win")
        hp = hp - 6
        print(hp)
        loose(hp)
        if hp < 1:
            break



