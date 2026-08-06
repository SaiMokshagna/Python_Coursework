'''s='Python Programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
        
        
l=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)


n=int(input('Enter a number:'))
fact=1
for i in range(1,n+1):
    fact=fact*i
    
print(f"Factorial of {n} is {fact}")



d={}
n=int(input("Enter number of students: "))
min_marks=float('inf')
for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter student marks: "))
    if min_marks > marks:
        min_marks=marks
    d[name]=marks
    
print(d)
print("Minimum marks is: ",min_marks)


d={}
n=int(input("Enter number of students: "))
max_marks=0
for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter student marks: "))
    if max_marks < marks:
        max_marks=marks
    d[name]=marks
    
print(d)
print("Maximum marks is: ",max_marks)


d={}
n=int(input("Enter number of products: "))
total_bill=0
for i in range(n):
    name=input("Enter product name: ")
    quantity=int(input("Enter product quantity: "))
    price=int(input("Enter product price: "))
    d[name]=price
    f_price=price*quantity
    total_bill += f_price
    d[name]=f"{name} : {quantity} * {price} = {f_price}"    
print(d)
print("Total bill is: ",total_bill)'''


n=int(input("Enter number of products: "))
total_bill=0
products={}
for i in range(n):
    product=input(f"Product - {i}: ")
    price=float(input(f"Price - {i}: "))
    quantity=int(input(f"Quantity - {i}: "))
    f_price=price*quantity
    total_bill += f_price
    products[product]=f"{quantity} * {price} = {f_price}"
print(products)
print("Total bill: ",total_bill)