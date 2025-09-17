#https://zestedesavoir.com/tutoriels/582/les-slices-en-python/#tableau-des-idiomes-sur-les-slices
p = "abcdefghij"
print (p [::-2][:5][:: -1][3:])
print()
#si on les met bout a bout ils se cumulent 
print (p [::-2])
print (p [::-2][:5])
print (p [::-2][:5][:: -1])
print()
print (p [::-2])
print (p [:5])
print (p [::-1])
print (p [3:])