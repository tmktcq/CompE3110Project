import math

def restoring(dividend, divisor): #Put in Print Statments later. 

    i = len(divisor)-1 # this is equal to the amout of shifts we will  have
    NotB = onesComplement(B)
    while( i > 0 ):
        if(i != len(divisor)-1):
            dividend = A + Q
        E,A,Q= shl(dividend)
        A = E+A
        print("shift: "+A,Q  )
        SavedA = A
        A = add(A,NotB)
        print("Add: " + A)
        if(A[0] == '0'):
            print("A>B no restore")
            Q = Q.replace('_','1')
            
        else:
            A = SavedA
            Q = Q.replace('_','0')
            print("A<B restore")
        i -= 1

    return A[1:len(A)] , Q 


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

def shl(dividend):
    E = dividend[1]
    A = dividend[2:(math.ceil((len(dividend)/2))+1)] #should be from [1:]
    Q = dividend[(math.ceil(len(dividend)/2)+1): len(dividend)]
    Q += "_"
    
    return E, A , Q 
    
dividend = "010100011" # has to be EAQ 
B = "01011"
print(restoring(dividend, B))