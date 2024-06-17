a = float(input("Enter your first num: " ))
todo =str(input('Enter your operation '))
if todo not in ['Square','square','*2']:
  b= float(input("Enter your 2nd num: " ))
if todo == 'add' or todo ==  'Add'or todo == '+':
   num1=a+b
   print('your answer = ',num1)
elif todo == 'substract' or todo =='sub'or todo == '-':
     num2= a-b
     print('your answer = ',num2)
elif todo == 'multiply' or todo== 'Multiply' or todo == '*':
    num3=a*b
    print('your answer = ',num3)
elif todo == 'Divide' or todo == 'divide'or todo == '/':
   if b!=0:
    num4=a/b
    print('your answer = ',num4)
   else :
    print('Error! Dvision by 0 is not valid')
elif todo == "Square" or todo == 'square' or todo == '*2':
  num5=a**2
  print('your answer = ',num5)
elif todo == 'Percentage' or todo == 'percentage' or todo == '%':
  num6=((a/b)*100)
  print('your answer = ',num6)
else :
 print('please enter any operation name or synmbol')