# input a first number from user and store in a
a = int(input("first number:"))
# input a function that perform by user
function = input("enter function +,-,*,/ :")
# input second number from user and store in b
b = int(input("second number:"))
# if function is equal to + then print 'a + b'
if function == "+":
    print(a + b)
# if function is not equal to '+' then check '-' and perform 'a- b'
elif function == "-":
    print(a - b)
# if function is not equal to '-' then check "*" and perform "a*b"
elif function == "*":
    print(a * b)
# if function is not equal to '*' then check "/"and perform "a / b"
elif function == "/":
# if function is not equal to "/" then print "ERROR"
    print(a / b)
else: print("ERROR")
