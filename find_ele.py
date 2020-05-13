def element(array):
    
    for x, v in enumerate(array):
        if array.count(v) == 1:
            return v

print(element([2,2,1]))
print(element([2,2,1,1]))
print(element([4,1,2,1,2]))
