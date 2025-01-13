def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("division with zero is not possible")
    else:
        return a/b
def calc():
    print("welcome to calc operations")
    print("list of operations given below and select which one u want:")
    print("1.addition,2.subtraction,3.multiplication,4.division,5.exit")
    while True:
        user_op=input("enter the choice(1/2/3/4/5):")
        if user_op in ['1','2','3','4']:
            a=float(input("enter first number:"))
            b=float(input("enter second number:"))
            if user_op=='1':
                print("addition result is:",add(a,b))
            elif user_op=='2':
                print("subtraction result is:",sub(a,b))
            elif user_op=='3':
                print("multiplication result is:",mul(a,b))
            elif user_op=='4':
                print("division result is:",div(a,b))
        elif user_op=='5':
                print("operation doesn't exist in calc")
                break
        else:
            print("invalid")
calc()
