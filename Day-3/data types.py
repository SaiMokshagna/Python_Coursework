Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count=10
>>> count
10
>>> type(count)
<class 'int'>
>>> price=99.99
>>> price
99.99
>>> type(price)
<class 'float'>
>>> c=9+8j
>>> c
(9+8j)
>>> type(c)
<class 'complex'>
>>> s='I am Sai'
>>> s
'I am Sai'
>>> type(s)
<class 'str'>
>>> l=['sai',1,2,1,3]
>>> l
['sai', 1, 2, 1, 3]
>>> print(l)
['sai', 1, 2, 1, 3]
>>> type(l)
<class 'list'>
>>> t=("sai",1,'weret')
>>> t
('sai', 1, 'weret')
>>> p=type(t)
>>> p
<class 'tuple'>
>>> s={1,2,5,2,5,6,3,'int','zxer'}
>>> s
{1, 2, 3, 'int', 5, 6, 'zxer'}
>>> print(type(s))
<class 'set'>
>>> s={}
>>> s
{}
>>> print(type(s))
<class 'dict'>
>>> d={"sai":"Moksha",'batch'=1}
SyntaxError: ':' expected after dictionary key
d={"sai":"Moksha","batch":1}
d
{'sai': 'Moksha', 'batch': 1}
type(d)
<class 'dict'>
stat=None
stat
type(stat)
<class 'NoneType'>
s=frozenset({1,2,3,5,6,9,7})
s
frozenset({1, 2, 3, 5, 6, 7, 9})
type(s)
<class 'frozenset'>
