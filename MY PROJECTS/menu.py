num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("  MENU  ")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choose=input("select operation(1/2/3/4):")
if choose=='1':
    result=num1+num2
    print("RESULT:",result)
elif choose=='2':
    result=num1-num2
    print("RESULT:",result)  
elif choose=='3':
    result=num1*num2
    print("RESULT:",result) 
elif choose=='4':
    result=num1/num2
    print("RESULT:",result)     




