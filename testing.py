import math

def divideOverflow(dividend, divisor):
    A = dividend[1:(math.ceil((len(dividend)/2)))] #should be from [1:]
    decDivisor = bin2dec((divisor[1::]))
    decA = bin2dec((A))
    if(decA >= decDivisor):
        return -1 
    else:
        return 0 

def bin2dec(binary):
    decimal = 0
    for digit in binary:
        decimal = (decimal*2 + int(digit))
    return decimal


dividend = "1111111000001"
divisor = "1111111"

print(divideOverflow(dividend,divisor))