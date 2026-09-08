file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close(0)

with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

with open('mysql.txt','w') as file:
    file.write('DDL,DML')
    
with open('pfs-63.txt','w') as file:
    file.write('Hello moto')

with open('pfs-63.txt','a') as file:
    file.write('Hello Python\n')
    
with open('pfs-63.txt','a+') as file:
    file.write("Tom same branch 5\n")
    file.seek(0)
    print(file.read())
    
with open('mysql.txt','w+') as file:
    file.write("Tom same branch 5\n")
    file.seek(0)
    print(file.read())
    
with open('mysql.txt','r+') as file:
    file.write("Tomorrow same branch 5\n")
    file.seek(0)
    print(file.read())