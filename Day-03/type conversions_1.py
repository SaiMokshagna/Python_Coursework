Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,'sai']
a
[1, 2, 'sai']
type(a)
<class 'list'>
int(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'list'
complex(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'list'
str(a)
"[1, 2, 'sai']"
tuple(a)
(1, 2, 'sai')
set(a)
{1, 2, 'sai'}
frozenset(a)
frozenset({1, 2, 'sai'})
dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
a={1,2,3,'sdf'}
a
{1, 2, 3, 'sdf'}
type(a)
<class 'set'>
int(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
str(a)
"{1, 2, 3, 'sdf'}"
list(a)
[1, 2, 3, 'sdf']
tuple(a)
(1, 2, 3, 'sdf')
fozenset(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    fozenset(a)
NameError: name 'fozenset' is not defined. Did you mean: 'frozenset'?
dict(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
type(a)
<class 'set'>
a=(1,2,3,4,5,6,'saom')
type(a)
<class 'tuple'>
int(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(a)
"(1, 2, 3, 4, 5, 6, 'saom')"
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> list(a)
[1, 2, 3, 4, 5, 6, 'saom']
>>> tuple(a)
(1, 2, 3, 4, 5, 6, 'saom')
>>> set(a)
{1, 2, 3, 4, 5, 6, 'saom'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> a={'a':123,'b':456}
>>> type(a)
<class 'dict'>
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> set(a)
{'a', 'b'}
>>> list(a)
['a', 'b']
>>> tuple(a)
('a', 'b')
>>> compex(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    compex(a)
NameError: name 'compex' is not defined. Did you mean: 'complex'?
>>> dict(a)
{'a': 123, 'b': 456}
