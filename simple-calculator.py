#CALCULATOR PYTHON

#program make a simple calculator

#this function add numbers
def add(x,y):
    return x+y

#this function substract numbers
def substract(x,y):
    return x-y

#this function multiple numbers
def multiple(x,y):
    return x*y

#this function divide numbers
def divide(x,y):
    return x/y

print("Select the operation.")
print("1. Add")
print("2. Substract")
print("3. Multiple")
print("4. Divide")

while True:
    #Take input from the user
    choice=input("Enter your choice(1/2/3/4) : ")

    #check if choice is one of the four
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        if choice=='1':
            print(num1,'+',num2, '=', add(num1, num2))

        elif choice=='2':
            print(num1,'-',num2, '=', substract(num1, num2))

        elif choice=='3':
            print(num1,'*',num2, '=', multiple(num1, num2))
            
        elif choice=='4':
            print(num1,'/',num2, '=', divide(num1, num2))
        break
    else:
        print("Invalid Input")