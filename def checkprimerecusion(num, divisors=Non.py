def checkprimerecusion(num, divisors=None):
    if divisors is None:
        divisors = num -1
    while divisors >= 2:
        if num % divisors == 0:
            return False
        else:
            return checkprimerecusion(num, divisors-1)        
    else:
        return True
given_num = int(input('Enter some random number ='))    
    
if(checkprimerecusion(given_num,)):
        print('the given number', given_num, 'is a prime number.')
else:
        print('The given number', given_num,'is not a prime number.')     
