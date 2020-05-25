def vow(word):
    vowels = ['a','e','i','o','u']
    vow_nums = [x for x in word if x in vowels]
    rev = list(reversed(vow_nums))
    count = 0
    lst = [n for n in word]
    for x, v in enumerate(lst):
        if v not in vowels:
            pass
        else:
            lst[x] = rev[count]
            count += 1
    fin_num = ''.join(str(x) for x in lst) 
    return fin_num

print(vow('code'))
print(vow('hello'))
print(vow('leetcode'))
            



