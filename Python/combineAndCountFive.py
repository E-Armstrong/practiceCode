def combineAndCountFive (arr1, arr2):
    numOfFives = 0
    elementInBoth = []
  
    numOfFives = arr1.count(5)
    numOfFives += arr2.count(5)
    lastElement = None

    for element in arr1:
        if (element in arr2) and (element not in elementInBoth):
            elementInBoth.append(element)
  
    return elementInBoth, numOfFives

array1 = [1,2,3,4,5,5,5,10,10]

array2 = [1,6,7,8,9,5]

print(combineAndCountFive(array1,array2))