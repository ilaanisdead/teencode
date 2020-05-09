def num(x):
    number = bin(x)
    nom = number.replace('0b','',1)
    comp = [int(x) for x in str(nom)]
    
    for n, i in enumerate(comp):
        if i == 1:
            comp[n] = 0
        else:
            comp[n] = 1
    
    fin = ''.join([str(ele)for ele in comp])
    return(int(fin, 2))

print(num(5))
