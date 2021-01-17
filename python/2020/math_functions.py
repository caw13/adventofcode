import math 
  
# get prime factors
def getPrimeFactors(n): 
    returnSet = set()  
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        returnSet.add(2)
        n = n // 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            returnSet.add(i)
            n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        returnSet.add(n)
    return returnSet 

# takes a dictionary of tuples, coprimes paired with arbitrary integers for the system of simultaneous congruences
# {n1:a1,n2:a2,n3:a3}
# x = a1 mod n1
# x = a2 mod n2
# x = a3 mod n3
# and returns the solution x
def chinese_remainder_theorem(tuplePairs):
    x = 0
    N = math.prod(tuplePairs.keys())
    for modNum, a in tuplePairs.items():
        y = N // modNum
        z = pow(y, -1, modNum)
        x += a * y * z
    return x % N

testSet = {3:2, 5:3, 7:2}
result = chinese_remainder_theorem(testSet)
print(str(result))