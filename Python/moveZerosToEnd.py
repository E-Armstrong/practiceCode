""" Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0] """

def move_zeros(array):
    y = len(array) - 1
    for x in reversed(array):
        if x is False:
            y = y 
        elif x == 0 or x == 0.0:
            array.pop(y)
            array.append(0)
        y = y - 1
    return array