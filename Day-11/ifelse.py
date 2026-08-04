username=input("Username: ")
password=input("Password: ")
if username=="admin" and password=="admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")
    
    
products=['laptop','mobile','watch']
search=input("Search Product: ")
if search in products:
    print("Product found")
else:
    print("Product not found")
    
    
bill=int(input("Enter the bill: "))
if bill>99:
    print("bill")
else:
    print("bill+30")