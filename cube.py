def cube(number):
    return number*number*number
def by_3(number):
    if number%3==0:
        return cube(number)
    else:
        print ("False")

print (by_3(9))
print (by_3(13))

def cube1(number1):
    return number1*number1
def by_4(number1):
    if number1%2==0:
        return cube1(number1)
    else:
        print ("False")

print (by_4(10))
print (by_4(17))