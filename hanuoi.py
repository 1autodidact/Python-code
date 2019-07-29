def fun(word):
    if len(word) ==0:
        newword = ''
        return newword
    else:
        newword = word[-1] + fun(word[:-1])
        return newword
print(fun(input()))
        
        
