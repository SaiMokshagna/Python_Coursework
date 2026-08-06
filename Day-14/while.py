'''
i=1
while i<=10:
    print(i)
    i+=1
    
i=10
while i>=1:
    print(i)
    i-=1
    
i=2
while i<=100:    
    print(i,end=' ')
    i+=2
    
s="Python Programming"
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
    
l=[1,0,0,0,2,3,4,5,56,12,0,12,0,13,0,0,0,16,0]
while 0 in l:
    l.remove(0)
print(l)

d={}
total_bill=0
while True:
    product=input("Enter product name (for exit): ")
    if product=="exit":
        break
    price=float(input("Enter product price: "))
    total_bill+=price
    d[product]=price
print(d)
print(total_bill)'''

i=0
while i<10:
    i+=1
    if i==15:
        break
    print(i,end=' ')
else:
    print("End of the loop")