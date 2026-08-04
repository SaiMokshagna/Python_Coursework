'''s="SAi Mokshagna"
f,r ch in s:
    if ch in "aeiouAEIOU":
        print(ch)
        

l=[12, 3, 4, 5,43,55,432,5678,44,56]
for i in l:
    if i%2==0:
        print(i, "Even")
    else:
        print(i, "Odd")
        
 
marks=(90,20,35,46,78,90,87,48)
for i in marks:
    if i>=35:
        print(i, "Pass")
    else:
        print(i, "Fail")


followers={"sai", 'sajid', 'mohammed', 'mukesh', 'sandeep', 'suresh'}
for i in followers:
    print(i)

    

bus={'s1':"Booked", 's2':"Available", 's3':"Available", 's4':"Booked"}
for seat in bus:
    if bus.get(seat)=="Available":
        print(seat,bus.get(seat))
        '''


n=int(input("Enter the table number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")