import math
from prettytable import PrettyTable # pip install prettytable to use library 

restoringTable = PrettyTable()
nonrestoringTable = PrettyTable()

restoringTable.field_names = ["E", "A" , "Q" , "Notes"]
nonrestoringTable.field_names = ["E", "A" , "Q" , "Notes"]

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
    i = len(divisor)-1 # this is equal to the amout of iterations we will  have
    NotB = onesComplement(divisor) #does 1 and twos comp 
    while( i > 0 ):
        if(i != len(divisor)-1):
            dividend = A + Q
        E,A,Q= shl(dividend)
        restoringTable.add_row([E,A,Q, "SHL"])
        A = E+A
        SavedA = A
        A = add(A,NotB)
        restoringTable.add_row([NotB[0],NotB[1::],"", "Add ~B"])

        if(A[0] == '0'):
            Q = Q.replace('_','1')   
            restoringTable.add_row([A[0],A[1::],Q, "E=0, A>B no restore Q0=1"])
        else:
            A = SavedA
            Q = Q.replace('_','0')
            restoringTable.add_row([A[0],A[1::],Q, "E=1, A<0 restore Q0=0"])
        i -= 1
    restoringTable.add_row(["",A[1::],(sign+Q), "Reminder and Quotient"])
    restoringTable.add_row(["", binToHexa((A[1::])), binToHexa(sign+Q), "Results in Hexidecimal" ])

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
    
def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
      
    # counter to check group of 4
    count = 1
      
    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
      
    # counter for hexadecimal number array
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
          
        # check if group of 4 completed
        if count % 4 == 0:
            
            # check if temp < 10
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
              
        # group of 4 is not completed
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
          
    # check if at end the group of 4 is not
    # completed
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
          
    # check at end the group of 4 is completed
    if count == 1:
        i = i-1

    final = ""
    while(i >=0):
        final += hexaDeciNum[i]
        i = i-1
       
    if(final == ""):
        final = "0"
    return final    


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

dividend = "001001101" # has to be EAQ 
B = "11011"

restoring(dividend, B)
print()
print(restoringTable)
print()
print(nonrestoring(dividend,B))