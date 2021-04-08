""" 
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result 
in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3 """

def rgb(r, g, b):
    import math
    
    def roundNum(number):
        if number < 0: 
            number = 0
        elif number > 255:
            number = 255
        return number
    
    def makeHex(value):
        if value > 9:
            if value == 10:
                value = "A"
            if value == 11:
                value = "B"
            if value == 12:
                value = "C"
            if value == 13:
                value = "D"
            if value == 14:
                value = "E"
            if value == 15:
                value = "F"
        return str(value)
    
    firstValue  = makeHex(math.floor(roundNum(r)/16))
    secondValue = makeHex(roundNum(r)%16)
    thirdValue  = makeHex(math.floor(roundNum(g)/16))
    forthValue  = makeHex(roundNum(g)%16)    
    fifthValue  = makeHex(math.floor(roundNum(b)/16))
    sixthValue  = makeHex(roundNum(b)%16)  
    
    return firstValue + secondValue + thirdValue + forthValue + fifthValue + sixthValue