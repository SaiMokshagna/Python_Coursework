Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
print(a)
b=float(a)
print(b)
SyntaxError: multiple statements found while compiling a single statement
a=10
a
10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
a=10.99
type(a)
<class 'float'>
int(a)
10
str(a)
'10.99'
complex(a)
(10.99+0j)
set(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
a=10+3j
type(a)
<class 'complex'>
int(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
'(10+3j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
b='sai'
type(a)
<class 'complex'>
int(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
type(b)
<class 'str'>
int(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: 'sai'
float(b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(b)
ValueError: could not convert string to float: 'sai'
>>> complex(b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(b)
ValueError: complex() arg is a malformed string
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
>>> tuple(b)
('s', 'a', 'i')
>>> list(b)
['s', 'a', 'i']
>>> set(b)
{'s', 'a', 'i'}
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a='123'
>>> type(b)
<class 'str'>
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: 'sai'
>>> int(a)
123
>>> float(a)
123.0
>>> complex(a)
(123+0j)
>>> tuple(a)
('1', '2', '3')
>>> list(a)
['1', '2', '3']
>>> set(a)
{'3', '1', '2'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
