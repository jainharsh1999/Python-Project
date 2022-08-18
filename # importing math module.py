import math
def checkPrimeNumber(number):
    if number < 1:
        return False
    
    max_divisor = math.floor(math.sqrt(number))
    for i in range(2, max_divisor+1):
        if number % i == 0:
            
              return False
        
        return True

number = 5

if(checkPrimeNumber(number)):
    print("The given number", number, "is prime number")
else:
    print("The given number", number, "is not prime number")