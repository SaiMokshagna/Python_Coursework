Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c='strings.py'
c.startswith('str')
True
c.endswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'Python'.isupper()
False
'PYTHON'.isupper()
True
'PYTHON12'.isupper()
True
c.isalpha()
False
c.isalnum()
False
's123'.isalnum()
True
's.123'.isalnum()
False
>>> '   '.isspace()
True
>>> '   k'.isspace()
False
>>> 'this is total'.istitle()
False
>>> 'This Is Title'.istitle()
True
>>> 'my@var'.isidentifier()
False
>>> '_is'.isidentifier()
True
>>> 
>>> l=[]
>>> l=list()
>>> l=[1,2,3.4,5,[1,2,3],('ert'),{1:2,3:8,5:7}]
>>> l
[1, 2, 3.4, 5, [1, 2, 3], 'ert', {1: 2, 3: 8, 5: 7}]
>>> l=[34,5,7,5,3]
>>> type(l)
<class 'list'>
>>> m=[4,5,6,7]
>>> l+m
[34, 5, 7, 5, 3, 4, 5, 6, 7]
>>> l+m*3
[34, 5, 7, 5, 3, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7]
>>> l[5]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l[5]
IndexError: list index out of range
>>> l=[3]
>>> l=[34,5,7,5,3]
>>> m=[4,5,6,7]
>>> l+m
[34, 5, 7, 5, 3, 4, 5, 6, 7]
>>> l[4]
3
>>> l[-1]
3
>>> l[2:]
[7, 5, 3]
>>> l[:2]
[34, 5]
>>> l[::-1]
[3, 5, 7, 5, 34]
