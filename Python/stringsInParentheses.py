"""You have string like this "abc(def) (xyz) ((mno))"

Find the deepest nested string in parenthesis.

So in this case mno

Anoher scenario will be "aaa(bbb(ccc)(ddd))"

This should return ['ccc','ddd'] """

def stringsInParenth (stringX):
    parenthLevel = 0
    highestValueParenth = 0
    finalResult = []
    tempResult = []
    tempDictionary = []

    for char in stringX:

        if char is "(":
            if tempResult is not []:
                tempString = ""
                for letter in tempResult:
                    tempString += letter
                tempDictionary.append([parenthLevel, tempString])
                tempResult = []
            parenthLevel += 1

        if char is ")":
            if tempResult is not []:
                tempString = ""
                for letter in tempResult:
                    tempString += letter
                tempDictionary.append([parenthLevel, tempString])
                tempResult = []
            parenthLevel -= 1

        if (parenthLevel > 0) and (char is not "(") and (char is not ")"):
            tempResult.append(char)
    
    if parenthLevel is not 0:
        return "Not equal amount of matching parenthesis."

    for keyPair in tempDictionary:
        if int(keyPair[0]) > highestValueParenth:
            highestValueParenth = int(keyPair[0])
    
    for keyPair in tempDictionary:
        if keyPair[0] is highestValueParenth:
            finalResult.append(keyPair[1])

    return finalResult

    

print(stringsInParenth("abc(def) (xyz) ((mno))"))

print(stringsInParenth("aaa(bbb(ccc)(ddd))"))

print(stringsInParenth("aaa(bbb((ccc))(ddd))"))

print(stringsInParenth("aaa(bbb(ccc)((ddd)))"))
