def array(num):
    array1 = [None]* len(num)
    n = 0
    m = 1
    for x in num:
        if x % 2 == 0:
            array1[n] = x
            n += 2
        else:
            array1[m] = x
            m += 2
    return array1
print(array([4,2,5,7])) 


