Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=input()
sai mokshagna
x
'sai mokshagna'
name=input()
Moksha
name
'Moksha'
name=input("enter your name:")
enter your name:Sai
name
'Sai'
age=int(input("Enter your age:"))
Enter your age:21
age
21
type(age)
<class 'int'>
age=inpit("Enter age:")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    age=inpit("Enter age:")
NameError: name 'inpit' is not defined. Did you mean: 'input'?
age=input("Enter age:")
Enter age:21
age
'21'
type(age)
<class 'str'>
names=input("Enter names:")
Enter names:sai mokshagna kumar
names
'sai mokshagna kumar'
names.split() #split() is used to separate the elements in the string.
['sai', 'mokshagna', 'kumar']
names=input("Enter names:").split()
Enter names:Sai Mokshagna Kumar
names
['Sai', 'Mokshagna', 'Kumar']
names=input("Enter names:").split()
Enter names:1 2 5 8 89 52
names
['1', '2', '5', '8', '89', '52']
map(int,names)
<map object at 0x000001A3969FECB0>
list(map(int,names))
[1, 2, 5, 8, 89, 52]
values=list(map(int,input().split()))
1 5 2 555 663 85
values
[1, 5, 2, 555, 663, 85]
names=tuple(map(int,input()>split()))
names=tuple(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    names=tuple(map(int,input()>split()))
NameError: name 'split' is not defined
names=tuple(map(int,input().split()))
sai mokshagna ravi
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    names=tuple(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'sai'
names=tuple(input("Enter names:").split())
Enter names:sai mokshagna krishna
names
('sai', 'mokshagna', 'krishna')
list(names)
['sai', 'mokshagna', 'krishna']
set(names)
{'krishna', 'sai', 'mokshagna'}
names=set(input("Enter names:").split())
Enter names:ram ravi rao
names
{'rao', 'ram', 'ravi'}
lsit(names)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lsit(names)
NameError: name 'lsit' is not defined
list(names)
['rao', 'ram', 'ravi']
tuple(names)
('rao', 'ram', 'ravi')
set(names)
{'rao', 'ram', 'ravi'}
str(names)
"{'rao', 'ram', 'ravi'}"
names=set(map(str,input().split()))
sai ram
names
{'sai', 'ram'}
#Taking multiple inputs
a,b=[1,2]
a
1
b
2
email,password=input("Enter the mail and password:").split()
Enter the mail and password:msm@gmail.com msm2345
emain
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    emain
NameError: name 'emain' is not defined. Did you mean: 'email'?
email
'msm@gmail.com'
password
'msm2345'
a,b,c=list(int,input().split())
1 2 3
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a,b,c=list(int,input().split())
TypeError: list expected at most 1 argument, got 2
a
1
b
2
b
2
c
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c
NameError: name 'c' is not defined
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks=input().split()
sai 87
name
'sai'
marks
'87'
int(marks)
87
>>> #Using eval()
>>> e=eval(input())
1
>>> e
1
>>> type(e)
<class 'int'>
>>> e=eval(input())
sai
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'sai' is not defined
>>> e=eval(input())
sai
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'sai' is not defined
>>> e=eval(input())
12.66
>>> e
12.66
>>> e=eval(input())
'sai'
>>> e
'sai'
>>> e=eval(input())
[1,2,3,4]
>>> e
[1, 2, 3, 4]
>>> type(e)
<class 'list'>
>>> e=eval(input())
{1,2,3,4}
>>> e
{1, 2, 3, 4}
>>> e=eval(input())
{'name':1,'Marks':2}
>>> e
{'name': 1, 'Marks': 2}
>>> type(e)
<class 'dict'>
