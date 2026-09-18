P1 = float(input("Price of HP Victus: "))
P2 = float(input("Price of Mac: "))
P3 = float(input("Price of asus vivobook: "))

# bill amount 

print("=="*32)
print("              Welcome to yashwant plaza DIGITAL MARKET")
print("=="*32)
product_name = ["HP victus","macbook air ", "Asus vivobook"]
product_name[0] = P1
product_name[1] = P2
product_name[2] = P3
print("Product Name "," "*30,"Price")
print("1. HP victus", end = " "*30 )
print(product_name[0])
print("2. Macbook air", end = " "*28 )
print(product_name[1])
print("3. Asus vivo book", end = " "*25 )
print(product_name[2])

print("--"*30)
bill = P1 + P2 + P3
print("Billing amount"," "*26, bill)
print("--"*30)
print("            Thank you for visiting ! Have great day")
print("=="*30)



