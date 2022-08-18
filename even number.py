totalCount = int(
    input("Enter the total number of elements of the given list = "))
given_list = []
for i in range(totalCount):
    eleme = int(input("Enter some random element(integer) = "))
    given_list.append(eleme)

evenNumList = []
oddNumList = []

for eleme in given_list:
  
    if(eleme % 2 == 0):
        evenNumList.append(eleme)
  
    else:
        oddNumList.append(eleme)

evenNumList.sort()

oddNumList.sort()
print("The Largest even number in the given list",
      given_list, "=", evenNumList[-1])
print("The Largest odd number in the given list",
      given_list, "=", oddNumList[-1])