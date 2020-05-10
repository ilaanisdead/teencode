def non_rep(word):

    for x,v in enumerate(word):

        if word.count(v) == 1:
            return x
    
    return -1

print(non_rep("leetcode"))
print(non_rep("loveleetcode"))
