# making a faulty calculator

# taking input from the user and changing into integer
print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('Choose One','+,-,/,%,*')
num3 =input()

if num1==45 and num2==3 and num3=='*':
    print("Result is : 555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("Result is : 77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("Result is : 4")
elif num1 == 54 and num2 == 30 and num3 == '-':
        print("Result is : 23")
elif num3=='*' :
    num4=num1*num2
    print("Result is :",num4)
elif num3 == '+':
    plus=num2+num1
    print("Result is :",plus)
elif num3 == '/':
    Dev=num2/num1
    print("Result is :",Dev)
elif num3 == '-':
    Subtract=num2-num1
    print("Result is :",Subtract)
elif num3 == '%':
    percent=num2%num1
    print("Result is :",percent)
else:
    print("Error! Please check your input")