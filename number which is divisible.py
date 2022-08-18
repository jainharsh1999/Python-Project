lowerlimit = 19
upperlimit = 1289

print("The number which is divisible by 7 and multiple of 5 :")
for numb in range(lowerlimit, upperlimit+1):
      if(numb % 7 == 0 and numb % 5 == 0):
        print('Number =',numb)