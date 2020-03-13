#even numbers
def even(lst):
    ret_val = lst
    return ret_val
for n in range(1,50):
    if (n % 2 == 0):
        print(even(n))
            
#odd numbers
def odd(tst):
    ret_value = tst
    return ret_value
for x in range(1,60):
    if x % 2 != 0:
        print(odd(x),end=" ")