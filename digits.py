# To find how many digits a number has based on user inputb5
x=int(input("Enter a number:"))
if x>=0 and x<10:
    print(x," is a 1 digit number")
elif x>=10 and x<100:
    print(x," is a 2 digit number")
elif x>=100 and x<1000:
    print(x," is a 3 digit number")
else:
    print(x," has 4 or more digits")