def palin(word):
    if type(word)== str:
        for n in word:
            if word == word[::-1]:
                word = True
            else:
                word = False
            return word
    else:
        print("enter a word")

print(palin("madam"))
print(palin(101))
