# https://www.pierre-giraud.com/python-apprendre-programmer-cours/operateur/
phrase = input("ecrire une phrase:")
phrase = phrase.lower()
b = phrase.split()
for c in b:
    print(c[0])
print(b[0])
# a refaire