
def productRecursion(firstnumb, secondnumb):
    if(firstnumb < secondnumb):
        return productRecursion(secondnumb, firstnumb)
    elif(secondnumb != 0):
        return(firstnumb + productRecursion(firstnumb, secondnumb-1))
    else:
        return 0


firstnumb = 27
secondnumb = 19

print("The product of the given numbers", firstnumb, 'and', secondnumb, 'is ' +
      str(firstnumb)+' * '+str(secondnumb)+' = ', productRecursion(firstnumb, secondnumb))