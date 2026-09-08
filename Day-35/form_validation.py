import re
fullname = input("Enter your full name: ")
pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
res = re.fullmatch(pattern, fullname)
print("Valid full name" if res else "Invalid full name")

email=input("Enter your email: ")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[A-Za-z]{2,}$'
res=re.fullmatch(pattern,email)
print("Valid email" if res else "Invalid email")

phonenumber=input("Enter your phone number: ")
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
res=re.fullmatch(pattern,phonenumber)
print("Valid phone number" if res else "Invalid phone number")

password=input("Enter your password: ")
pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res=re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")

username = input("Enter your username: ")
pattern = r'^[A-Za-z_][A-Za-z0-9_.]{4,}$'
res = re.fullmatch(pattern, username)   
print("Valid username" if res else "Invalid username")

aadhar_number=input("Enter your Aadhar number: ")
pattern=r'^\d{12}$'
res=re.fullmatch(pattern,aadhar_number)
print("Valid Aadhar number" if res else "Invalid Aadhar number")

Pan_number=input("Enter your PAN number: ")
pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]$'
res=re.fullmatch(pattern,Pan_number)
print("Valid PAN number" if res else "Invalid PAN number")