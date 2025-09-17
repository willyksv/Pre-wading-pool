""""
Write 3 functions, each taking a string s and an integer n as parameters and returning a boolean:
✓ funA checks if s contains at least n characters;
✓ funB checks if s contains at least n special characters;
✓ funC checks if s contains at least n numbers.
"""

# def fun_a(s,n): 
#     return len(s) >= n
# print(fun_a('babba', 5))


# import string
# print(string.punctuation)
# def fun_b (s, n):

# s = "je, suis"
# for string.punctuation in s:
#     len(string.punctuation)

lestring = "Text123"

lelist = ["Text", "foo", "bar"]

for x in lelist:
    if lestring.count(x):
        print ('Yep. "%s" contains characters from "%s" item.' % (lestring, x))
