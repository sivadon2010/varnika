# addition
a = int(input('enter the number'))
b = int(input('enter the number'))
c = a+b;
s = a-b;
m = a*b;
d = a/b;
print("addition:",c)
print('subraction:',s)
print('multiplication: ', m)
print("divide: ",d)
#arithmetic opertions
# % IS USED TO GET A REMINDER OF  DIVIDER
remain = a % b
print("remainder: ",remain)
# ** its a exponenet
expo =  a ** 5
print("exponential value: " ,expo)
#abs() absolute value is operator which is used to return the value in positive only
print("absolute value: ", abs(s))
#round() operator is used to round off the input value
print("round value: ",round(d))
#mathematic precedance
value = (a + b) ** remain * expo - d
print("answer: ", value)







