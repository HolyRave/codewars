def dup(arry):
    newword = ''
    array2 = []
    for word in arry:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                newword += word[i]
        newword += word[-1]
        array2.append(newword)
        newword = ''
    return array2
