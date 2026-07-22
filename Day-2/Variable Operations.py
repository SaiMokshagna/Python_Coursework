Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a
10
>>> b
10
>>> a,b=ba
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a,b=ba
NameError: name 'ba' is not defined. Did you mean: 'a'?
>>> a,b=b,a
>>> a
10
>>> b
10
>>> a=10
>>> b=20
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
