def add(x, y):
 return (x+y)
def sub(x, y):
 return (x-y)
def mul(x, y):
 return (x*y)
def div(x, y):
 return (x/y)
op = raw_input("Enter a character ")
a = int(input("enter first number "))
b = int(input("enter second number "))

if op == '+':
   print(a,"+",b,"=", add(a,b))
elif op == '-':
   print(a,"-",b,"=",sub(a,b))
elif op == '*':
   print(a,"*",b,"=",mul(a,b))
elif op == '/':
   print(a,"/",b,"=",divide(float(a),float(b)))
else:
   print("WRONG CHARACTER ENTERED")
   