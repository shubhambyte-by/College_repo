# Using IF - ELIF - ELSE

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Excellent")

elif marks >= 60:
    print("Good")
elif marks < 40:
    print("fail")
else:
    print("Need improvement")