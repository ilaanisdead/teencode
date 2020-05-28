from collections import Counter
def str_1(s):
   lst_1 = Counter(s)
   lst = lst_1.most_common()
   lst_2 = [x[0]*x[1] for x in lst]
   return lst_2


print(str_1('tree'))
print(str_1('people'))
print(str_1('happy'))