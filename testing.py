''' Created this for testing functions individually '''

A = "10100011"

def shl(dividend):
    dividend +="_"
    E = dividend[0]
    A = dividend[1:int((len(dividend)-1)/2)] #should be from [1:]
    Q = dividend[int(len(dividend)/2): len(dividend)]

    return E, A , Q 
print(A)
print(shl(A))