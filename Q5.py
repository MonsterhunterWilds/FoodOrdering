num1=int(input('Please enter the first number: '))
num2=int(input('Please enter the second number: '))
print('-----Calculator-----')
print('1-Summation')
print('2-Substraction')
print('3-Multiplication')
print('4-Division')
opt=int(input('Choose the operation: '))

if(opt == 1):
    result=num1+num2
    print('The summation of the two number is: ',result)

elif(opt == 2):
    result=num1-num2
    print('The substraction of the two number is: ',result)

elif(opt == 3):
    result=num1*num2
    print('The multiplication of the two number is: ',result)

elif(opt == 4):
    result=num1/num2
    print('The division of the two number is: ',result)

else:
    print('Please enter choices 1-4')
