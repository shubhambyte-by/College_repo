# Let x=3, y = 4, find (x**y)*5 <50 and x > 39 =?
# x = 3
# y = 4
# print("Answer is: ", (x**y)*5 < 50 and x > 39)

# Let marks = 50, Find ("Pass") if (marks >= 50) else("Fail")=?
# marks = 50
# if marks >= 50:
#     print("Pass")
# else:
#     print("Fail")    


# (10 + 5) * 2 > 20 and 4 !=5 = ?

# if (10 + 5) * 2 > 20 and 4 != 5:
#     print("True")
# else:
#     print("False")    

# Let x=8, y = 6, find (x & y + 2) if (x | y > 12) else ((x ^ y) << (x % y))=?

x = 8
y = 6 

if(x|y>12):
    print(x & y + 2)
else:
    print((x ^ y) << (x % y))