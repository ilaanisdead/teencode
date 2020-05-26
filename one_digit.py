def one_dig(num):
   
    lst = [int(x) for x in str(num)]
    count = 0
    for x in lst:
        count += x
    lst_2 = [int(x) for x in str(count)]
    if sum(lst_2) >= 10:
        lst_3 = [int(x) for x in str((sum(lst_2)))]
        return sum(lst_3)
    return sum(lst_2)

print(one_dig(38))
print(one_dig(5788))
print(one_dig(68))