import math
a=float(input("enter a:"))
b=float(input("enter b:"))
x=float(input("enter x:"))

op=input("Enter op(+ ,- , * , / , sin , cos , tan , cot , factorial , sqrt):")

if op=="+":
    r=a+b
if op=="-":
    r=a-b
if op=="*":
    r=a*b
if op=="/":
    if b==0:
        r="error"
    else:
        r=a/b   
if op=="sin":
    r=(math.sin(math.radians(x)))
if op=="cos":
    r=(math.cos(math.radians(x)))
if op=="tan":
    r=(math.tan(math.radians(x)))
if op=="cot":
    r=(1)/(math.tan(math.radians(x)))
if op=="factorial":
    r=(math.factorial(x))
if op=="sqrt":
    r=(math.sqrt(x))
print(r)

