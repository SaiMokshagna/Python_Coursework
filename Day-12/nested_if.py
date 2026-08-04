'''fa=eval(input("Follows account:"))
cf=eval(input("Close friend: "))
if fa:
    if cf:
        print("Story visible")
    else:
        print("Not in close friend list")
        
elif fa==False and cf==True:
    print("Follow the account first")
else:
    print("Follow the account first")



Reg=eval(input("Enter registered or not:"))
fp=eval(input("Enter fee paid or not:"))
if Reg==True:
    if fp:
        print("Entry confirmed ")
    else:
        print("Entry fee pending")
elif Reg==False and fp==True:
    print("Register first")
else:
    print("Registration required")



Reg=eval(input("Enter registered or not:"))
if Reg:
    fp=eval(input("Enter fee paid or not:"))
    if fp:
        print("Entry confirmed ")
    else:
        print("Entry fee pending")

else:
    print("Registration required")
'''


act=eval(input("Link active: "))
if act:
    pg=eval(input("Enter the pg: "))
    if pg:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Invalid file link")