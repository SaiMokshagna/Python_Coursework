#Positional Arguments:
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')
    
display('xyz','xyz@gmail.com','xyz@123')
display('xyz@123','xyz','xyz@gmail.com')
display('xyz@gmail.com','xyz','xyz@123')

#Keyword argument
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='ram',email='ram@gmail.com',password='ram@3412*')
display(password='sai12*',email='sai@gmail.com',name='sai')
display(email='rao@gmail.com',password='rao12*',name='rao')

#Default argument
def display(name,email='gmail.com',password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='krishna',email='krishna@gmail.com',password='krishna12*')
display(password='bala12*',name='bala')
display(email='sai@gmail.com',name='sai')

#Var length argument
def display(*names):
    print(names)
display('Moksha')
display('Moksha','Bala')
display('Moksha','Bala','Rao')
display('Moksha','Bala','Rao','Sekhar')