def missing(lst):
    lst_all=[]
    for n in lst:
        if n <= -1:
            pass
        else:
            lst_all.append(n)
    for num in range(max(lst)):
        if num not in lst_all:
            print(num)
            break
        else:
            pass
    
missing([0,1,3,4,5])
missing([-1,-2,1,2,3,5,0])