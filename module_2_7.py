def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1,'мысль')
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['питон', False]
values_dict = {'c':'Миру-мир'}

print_params(*values_list, **values_dict)

values_list_2 = ['правда', 'false']
print_params(*values_list_2, 42)

