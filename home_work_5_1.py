import keyword

my_var = str(input("Enter name var: "))
if my_var in keyword.kwlist or my_var.count('_') > 1 or not my_var.islower() or my_var[0].isdigit():
    print(False)
else:
    print(True)