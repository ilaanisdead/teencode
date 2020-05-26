def str_1(s):
    str_2 = s.split()
    if len(str_2) > 1:
        return len(str_2[-1])
    return 0 


print(str_1('Hello World'))
print(str_1('Hello'))
print(str_1('Holiday Program Uganda'))
