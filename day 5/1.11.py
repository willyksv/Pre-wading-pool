my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list . extend ( my_second_list )
print(my_first_list)
# "concatene" les 2 listes

my_first_list = [7 , 8 , 9]
my_second_list = [4 , 5 , 6]
my_first_list = [* my_first_list , * my_second_list ]
print(my_first_list)
# idem que 