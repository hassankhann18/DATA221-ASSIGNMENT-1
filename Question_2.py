def buildStringDictionary(stringList):
    result = {}

    for word in stringList:
        lengthOfWord = len(word)

        if lengthOfWord % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        result[word] = {
            "length": lengthOfWord,
            "parity": parity
        }

    return result
