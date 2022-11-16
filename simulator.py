from collections import deque


def main(): 
    D = "101"
    sum = add(D,D)
    print(sum)
    '''Ask professor if length can be an issue
    while(yes):
        dividend = input("input the dividend")
        divisor = input("input the divisor")
        restoring(dividend, divisor)
        Usercontinue = input("Y/N")
        if Usercontinue == 'Y':
            yes = True
        else:
            yes = False
    #Make a Function to check for divide overflow 
    Takes in two binary signed numbers 
        (9  ≤  dividend  length  ≤  25  and  5  ≤  divisor  length  ≤ 13)
    '''

def restoring(dividend, divisor): 
    placeholder = "empty" 

def nonrestoring(): 
    placeholder = "empty"    

def bin2dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def shiftLeft(D):
    D += " "
    eBit = D[0]
    D= D[1:]
    return D, eBit
    
def sub(D,B): # Fix this
    '''Add in Inverse here '''
    #Put adding after getting 2's complemnt. 
    

def onesComplement(num):
    oneComp = 0
    oneCompStr = ""
    for i in num:
        oneComp = 1^int(i)
        oneCompStr += str(oneComp)

    oneCompStr = twosComplement(oneCompStr)
    return oneCompStr

def twosComplement(num):
    fill = len(num)
    one = "1"
    one = one.zfill(fill)
    sum = (add(num,one)) 
    return sum


def add(num1,num2):
    i = len(num1) -1

    result = ''
    carry = 0

    while(i >= 0):
        sum = int(num1[i]) + int(num2[i])
        if sum == 2: #1 + 1
            if carry == 1:# 1+ 1 + carry 
                carry = 1
                result += '1'
            else: #1 + 1 
                carry = 1
                result += '0'
        elif sum == 1: # 1 + 0 or 0 + 1 case
            if carry == 1: # 1 + 0 + carry
                carry = 1
                result += '0'
            else: # 1 + 0
                carry = 0
                result += '1'
        elif sum == 0: # 0 + 0 case
            if carry == 1: # 0 + 0 + carry 
                carry = 0
                result += '1'
            else: # 0 + 0
                carry = 0
                result += '0'
        i -= 1
    result = result[::-1]
    return result

#shift using slice(1,len(string)) add in what E is with string+= 0 or 1

main() 