def listlengthRecursion(given_list):
    if not given_list:
        return 0
    return 1 + listlengthRecursion(given_list[1::2]) + listlengthRecursion(given_list[2::2])


given_list = [929, 138, 3, 193, 11, 1, 2, 3, 41,
              132, 56, 11, 917, 212, 455, 2235, 1, 1, 2, 3]

print('The given list is :')
print(given_list)
print("The length of the given list = ", listlengthRecursion(given_list))