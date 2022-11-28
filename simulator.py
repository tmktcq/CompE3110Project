import math


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

def restoring(dividend, divisor): #Put in Print Statments later. 
    sign = int(dividend[0]) ^ int(divisor[0])
    sign = str(sign)
    divisor = "0" + divisor[1::]
    divisor = "0" + divisor[1::]
    i = len(divisor)-1 # this is equal to the amout of shifts we will  have
    NotB = onesComplement(divisor) #does 1 and twos comp 
    print("  " + dividend + " = Dividend  " + divisor + " = divisor" )
    print()
    while( i > 0 ):
        if(i != len(divisor)-1):
            dividend = A + Q
            print( "  " +dividend + " = Dividend")
        E,A,Q= shl(dividend)
        A = E+A
        print( "  " + A,Q + "   Shift left")
        SavedA = A
        A = add(A,NotB)
        print(" +" + NotB)
        print(" =" + A , end ="  ")
        if(A[0] == '0'):
            print(" E=0, A>B no restore Q0=1")
            Q = Q.replace('_','1')   
        else:
            A = SavedA
            Q = Q.replace('_','0')
            print("E=1, A<0 restore Q0=0")
        i -= 1

    return A[1:len(A)] , (sign+Q)  # adds sign into the Quotient 
    return A[1:len(A)] , (sign+Q)  # adds sign into the Quotient 

def nonrestoring(dividend, divisor): 
    i = len(divisor)-1 # this is equal to the amout of shifts we will  have
    NotB = onesComplement(B)
    E = "0"
    while( i > 0):
        if(i != len(divisor)-1):
            dividend = A + Q
    
        if(dividend[0] == "1"):
            E,A,Q= shl(dividend)
            print("Shift: " + E,A,Q)
            A = E+A
            A = add(A,B)
            print("Add: " + A)
        else:
            E,A,Q= shl(dividend)
            print("Shift: " + E,A,Q)
            A = E+A
            A = add(A,NotB)
            print("Subtract: " + A)
        if(A[0] == '0'):
            Q = Q.replace('_','1')
        else:
            Q = Q.replace('_','0')
        i-=1
    if(A[0] == "1"):
        A = add(A,B)
    return A[0], A[1:len(A)] , Q 
        
def bin2dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def shl(dividend):
    E = dividend[1]
    A = dividend[2:(math.ceil((len(dividend)/2))+1)] #should be from [1:]
    Q = dividend[(math.ceil(len(dividend)/2)+1): len(dividend)]
    Q += "_"
    
    return E, A , Q 
    
def sub(D,B): # Fix this
    '''Add in Inverse here '''
    #Put adding after getting 2's complemnt. 
    return 0 

    return 0 

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

#shift using slice(1,len(string)) add in what E is with string += 0 or 1

dividend = "1000011100001000100100000" # has to be EAQ 
B = "0000011100000"
dividend = "1000011100001000100100000" # has to be EAQ 
B = "0000011100000"

print(restoring(dividend, B))
print()
print(nonrestoring(dividend,B))