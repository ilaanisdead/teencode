listOne = [3,6,9,12,15,18]
listTwo = [4,8,12,16,20,24,28]

lst_even = listOne[1:6:2]
lst_odd = listTwo[0:7:2]
lst_even.extend(lst_odd)
print(lst_even)