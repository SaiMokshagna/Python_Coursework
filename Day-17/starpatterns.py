''''
#M
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i+j==n-1 and i<=m or i==j and i<=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#N
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#O    
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#P
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m or j==n-1 and i<m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#Q
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 and i<n-1 or j==n-1 or i==n-2 or i>=m or j>=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#R
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 and i<m or i==m or i==j and i>=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#S
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==m or j==0 and i<m or j==n-1 and i>m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#X
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#V
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#Z
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j+i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#W  
n=int(input('Enter the values: '))
m = n//2 #j==0 or j==n-1 or i+j==n-1 and i<=m or i==j and i<=m
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or j+i==n-1 and i>=m or i+j==n+2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()