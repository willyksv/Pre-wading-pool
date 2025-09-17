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
print(word)