""" Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]] """

def multiplication_table(size):
    fullMatrix = []
    topRow = []
    
    for x in range(size):
        topRow.append(x + 1)
        
    for x in topRow:
        newRow = [];
        for y in topRow:
            newRow.append(x*y)
        fullMatrix.append(newRow)
        
    return fullMatrix