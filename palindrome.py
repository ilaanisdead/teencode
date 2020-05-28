def palin(word):
    if type(word) != int:
        if word == word[::-1]:
            return True
        return False
    else:
        print('Enter a word')
print(palin("madam"))
print(palin(101))

