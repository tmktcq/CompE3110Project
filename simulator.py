''' 
    Names: Tim Kellermann, Sudeep Potluri
    Project: Restoring vs. Nonrestoring division Algorithm
    Due Date: 11/29/2022
    file name: simulator.py 
'''

import math
from prettytable import PrettyTable # pip install prettytable to use library 

'''
   +---------------------------------------------------+
   |                                                   |
   |                 Global Variables                  |
   |                                                   |
   +---------------------------------------------------+
'''

restoringTable = PrettyTable()
nonrestoringTable = PrettyTable()
metricsTable = PrettyTable()

restoringTable.field_names = ["E", "A" , "Q" , "Notes"]
nonrestoringTable.field_names = ["E", "A" , "Q" , "Notes"]
metricsTable.field_names = ["Length of Dividend", "Length of Divisor" ,"Iterations", "Non-Restoring Add/Sub Count" , "Restoring Add/Sub Count"]

dividend = "010100011" # has to be EAQ 
B = "01011"

'''
   +---------------------------------------------------+
   |                                                   |
   |               Function Definitions                |
   |                                                   |
   +---------------------------------------------------+

   Purpose: Executes the Restoring division algorithm and logs steps taken.
   Pre-Conditions: input dividend as EAQ, and Divisor
   Post-Conditions: returns the number of additions/subtractions 
'''
def restoring(dividend, divisor): 

    restAddSubCount = 0
    sign = int(dividend[0]) ^ int(divisor[0]) #calculates sign bit
    sign = str(sign)
    divisor = "0" + divisor[1::]

    #divide overflow check
    if(divideOverflow(dividend,divisor)):
        restoringTable.add_row([" Divide Overflow has occured"," First half of A>=B","", ""])
        return "Divide Overflow"
    
    i = len(divisor)-1 # this is equal to the amout of iterations we will  have
    NotB = onesComplement(divisor) #does 1 and twos comp 
    while( i > 0 ):
        if(i != len(divisor)-1):
            dividend = A + Q
        E,A,Q= shl(dividend) #Shift left 
        restoringTable.add_row([E,A,Q, "SHL"])
        A = E+A
        SavedA = A
        A = add(A,NotB)
        restoringTable.add_row([NotB[0],NotB[1::],"", "Add ~B"]) #this is used to log steps 
        restAddSubCount = restAddSubCount + 1 #increments the addition counter
        if(A[0] == '0'):
            Q = Q.replace('_','1')   
            restoringTable.add_row([A[0],A[1::],Q, "E=0, A>B no restore Q0=1"]) #this is used to log steps 
        else:
            A = SavedA
            Q = Q.replace('_','0')
            restoringTable.add_row([A[0],A[1::],Q, "E=1, A<0 restore Q0=0"]) #this is used to log steps 
            restAddSubCount +=1 #increments the addition counter
        i -= 1
    restoringTable.add_row(["",A[1::],(sign+Q), "Reminder and Quotient"]) #Solution in binary
    restoringTable.add_row(["", binToHexa((A[1::])), binToHexa(sign+Q), "Results in Hexidecimal" ]) #Solution in hexadecimal
    return restAddSubCount

''' 
   Purpose: Executes the non-Restoring division algorithm and logs steps taken.
   Pre-Conditions: input dividend as EAQ, and Divisor
   Post-Conditions: returns the number of additions/subtractions 
'''
def nonrestoring(dividend, divisor): 
    nonrestAddSubCount = 0
    sign = int(dividend[0]) ^ int(divisor[0]) #calculates sign of quotient
    sign = str(sign)
    divisor = "0" + divisor[1::]
    dividend = "0" + dividend[1::]

    #divide overflow check
    if(divideOverflow(dividend,divisor)):
        nonrestoringTable.add_row([" Divide Overflow has occured"," First half of A>=B","", ""])
        return "Divide Overflow"
    
    i = len(divisor)-1 # this is equal to the amout of shifts we will  have
    NotB = onesComplement(divisor)
    E = "0"
    while( i > 0):
        if(i != len(divisor)-1):
            dividend = A + Q
    
        if(dividend[0] == "1"):
            E,A,Q= shl(dividend)
            nonrestoringTable.add_row([E,A,Q, "SHL"]) #this is used to log steps 
            A = E+A
            A = add(A,divisor)
            nonrestAddSubCount +=1 #increments the addition counter
            nonrestoringTable.add_row([divisor[0],divisor[1::],"", "Add B"]) #this is used to log steps 
        else:
            E,A,Q= shl(dividend)
            nonrestoringTable.add_row([E,A,Q, "SHL"])
            A = E+A
            A = add(A,NotB)
            nonrestAddSubCount +=1 #increments the addition counter
            nonrestoringTable.add_row([NotB[0],NotB[1::],"", "Add ~B"]) #this is used to log steps 
        if(A[0] == '0'):
            Q = Q.replace('_','1')
            nonrestoringTable.add_row([A[0],A[1::],Q, "E=0, Q0=1"]) #this is used to log steps 
        else:
            Q = Q.replace('_','0')
            nonrestoringTable.add_row([A[0],A[1::],Q, "E=1, Q0=0"]) #this is used to log steps 
        i-=1
    if(A[0] == "1"):
        nonrestoringTable.add_row([divisor[0],divisor[1::],"", "Add B"]) #this is used to log steps 
        nonrestAddSubCount +=1 #increments the addition counter
        A = add(A,divisor)

    nonrestoringTable.add_row(["",A[1::],(sign+Q), "Reminder and Quotient"]) #Result in Binary 
    nonrestoringTable.add_row(["", binToHexa((A[1::])), binToHexa(sign+Q), "Results in Hexidecimal" ]) #Result in Hexadecimal 
    return nonrestAddSubCount
        
''' 
   Purpose: converts binary to decimal
   Pre-Conditions: input a string that is binary
   Post-Conditions: returns the decimal equivalent
'''
def bin2dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

''' 
   Purpose: checks if divide overflow has occured
   Pre-Conditions: input dividend and divisor
   Post-Conditions: returns a bool if true then terminate program
'''
def divideOverflow(dividend, divisor):
    A = dividend[1:(math.ceil((len(dividend)/2)))]
    decDivisor = bin2dec((divisor[1::]))
    decA = bin2dec((A))
    if(decA >= decDivisor): # correlates to the partial Remainder greater than divisor 
        return True
    else:
        return False

''' 
   Purpose: shifts the binary number left 
   Pre-Conditions: input binary string
   Post-Conditions: returns EAQ from the shift
'''
def shl(dividend):
    E = dividend[1]
    A = dividend[2:(math.ceil((len(dividend)/2))+1)] # takes the upper half of bits 
    Q = dividend[(math.ceil(len(dividend)/2)+1): len(dividend)] # takes the lower half 
    Q += "_" # adds a buffer as Q0
    
    return E, A , Q 
    
''' 
   Purpose: converts binary to hexadecimal
   Pre-Conditions: input binary string
   Post-Conditions: returns the hexadecimal equavalent 
'''
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

''' 
   Purpose: calculates inverse 
   Pre-Conditions: input binary string
   Post-Conditions: returns the inverse as 2's comp
'''
def onesComplement(num):
    oneComp = 0
    oneCompStr = ""
    for i in num:
        oneComp = 1^int(i)
        oneCompStr += str(oneComp)

    oneCompStr = twosComplement(oneCompStr) #adds 0x01 for twos comp 
    return oneCompStr

''' 
   Purpose: calculates 2's comp
   Pre-Conditions: input binary string
   Post-Conditions: returns the inverse as 2's comp
'''
def twosComplement(num):
    fill = len(num)
    one = "1"
    one = one.zfill(fill) #fills the leading positions with 0's
    sum = (add(num,one)) 
    return sum

''' 
   Purpose: addition function used in both restoring and nonrestoring
   Pre-Conditions: input two binary numbers
   Post-Conditions: returns the sum of both binary numbers
'''
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


'''
   +---------------------------------------------------+
   |                                                   |
   |             Print Steps of Operation              |
   |                                                   |
   +---------------------------------------------------+
'''

restAddSubCount = restoring(dividend, B) #logs all of the Restoring Steps
nonRestAddSubCount = nonrestoring(dividend,B) #logs all of the nonRestoring Steps 
metricsTable.add_row([len(dividend), len(B), len(B)-1, nonRestAddSubCount, restAddSubCount]) #logs the counts of each algorithm

print("\n")
print("+---------------------------------------------+")
print("|                                             |")
print("|             Restoring Algorithm             |")
print("|                                             |")
print("+---------------------------------------------+")
print(restoringTable)
print("\n")

print("+-------------------------------------------+")
print("|                                           |")
print("|           Non-Restoring Algorithm         |")
print("|                                           |")
print("+-------------------------------------------+")
print(nonrestoringTable)
print("\n")
print(metricsTable)