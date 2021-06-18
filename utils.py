def listDictionary(file):
    listedWords =[]
    text = open(file)
    for word in text.readlines():
        listedWords.append(word[:-1])
    return listedWords
