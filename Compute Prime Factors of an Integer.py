numb = 300

print("The prime factors of the given number are : ")
value = 1
while(value <= numb):
    k = 0
    if(numb % value == 0):
        j = 1
        while(j <= value):
            if(value % j == 0):
                k = k+1
            j = j+1
        if(k == 2):
            print(value)
    value = value+1