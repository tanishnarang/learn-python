import time 
print("hey there, i am a calculator bot\nyou can use me to perform simple calculations")
time.sleep(4)

what=input("what do you wanna do :- sum , substraction , multiplication , divide\n:-")
time.sleep(1)
a=int(input("enter first number:"))
time.sleep(1)
b=int(input("enter second number:"))
if what == "sum":
    print("sum of given two numbers is:",a+b)
elif what == "substraction":
    if a >= b:
        print("substraction of two numbers",a-b)
    else :
        print("a is smaller then b","\nchoose another value by using again")
elif what == " multiplication" :
    print ("multiplication of two given numbers is:",a*b)
elif what == "divide" :
    if a>b :
        print ("dividing ",a,"by",b,"is:",a/b)
    else :
        print("a is not grater then b""\nchoose another value by using again")
else :
    print ("i have not learnt such calculation yet \nplease inform me about this calculation \ni will fix it someday")
time.sleep(5)
print("thankyou for using my calculator\nyou can use my calculator anytime later")
