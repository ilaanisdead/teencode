def one_dig(num):
    
    nums = [int(x) for x in num]
    count = 0
    for x in nums:
        count += x
    pol = str(count)
    fin_ans = [int(x) for x in pol] 
    if sum(fin_ans) <= 9:
        return sum(fin_ans)

print(one_dig('38'))
print(one_dig('5788'))
print(one_dig('68'))