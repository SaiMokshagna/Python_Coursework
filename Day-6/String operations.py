Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c="Python programming"
c
'Python programming'
len(c)
18
ord('P')
80
ord('p')
112
chr(65)
'A'
chr(54)
'6'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 't', 'y']
c.capitalise
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c.capitalise
AttributeError: 'str' object has no attribute 'capitalise'. Did you mean: 'capitalize'?
c.capitalise()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c.capitalise()
AttributeError: 'str' object has no attribute 'capitalise'. Did you mean: 'capitalize'?
c.capitalize()
'Python programming'
c.upper()
'PYTHON PROGRAMMING'
c.lower()
'python programming'
c.caseswap()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c.caseswap()
AttributeError: 'str' object has no attribute 'caseswap'
c.swapcase()
'pYTHON PROGRAMMING'
c.casefold()
'python programming'
s=""STRAẞEMÁLAGAÅngströmCafé"
SyntaxError: unterminated string literal (detected at line 1)
s="STRAẞEMÁLAGAÅngströmCafé"
s
'STRAẞEMÁLAGAÅngströmCafé'
s.casefold()
'strassemálagaångströmcafé'
c="String is immutable"
c
'String is immutable'
c.center(40,'#')
'##########String is immutable###########'
c.ljust(40,'_')
'String is immutable_____________________'
c.rjust(50,'*_*')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    c.rjust(50,'*_*')
TypeError: The fill character must be exactly one character long
c.rjust(50,'*')
'*******************************String is immutable'
'12'.zfill(4)
'0012'
c.find('p')
-1
c.find('s')
8
c.rfind('m')
12
c.lfind('i')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c.lfind('i')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
c.index('i')
3
c.index('m')
11
c.rindex('u')
13
c.count('m')
2
c.count('i')
3
c.replace('i','I')
'StrIng Is Immutable'
c.replace('StrIng','STRING')
'String is immutable'
c.replace('String','STRING')
'STRING is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.split()
['String', 'is', 'immutable']
'String', 'is', 'immutable'
('String', 'is', 'immutable')
'String', 'is', 'immutable'.split()
('String', 'is', ['immutable'])
'String, is, immutable'.split()
['String,', 'is,', 'immutable']
'String, is, immutable'.split(',')
['String', ' is', ' immutable']
'String is immutable'.rsplit(',')
['String is immutable']
'String, is, immutable'.rsplit(',')
['String', ' is', ' immutable']
s='''
Python
is Programming'''
s='''
Python
isProgramming'''
s='''
Python
is'''
s='''python
is
... programming'''
>>> s
'python\nis\nprogramming'
>>> s.splitlines()
['python', 'is', 'programming']
>>> ''.join(['','python','programming','lang'])
'pythonprogramminglang'
>>> '-'.join(['','python','programming','lang'])
'-python-programming-lang'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java,python,ruby'
>>> s.partition(',')
('java', ',', 'python,ruby')
>>> s.rpartition(',')
('java,python', ',', 'ruby')
>>> s='java,python,ruby'
>>> s.rpartition(',')
('java,python', ',', 'ruby')
>>> c='Hello Python'
>>> c
'Hello Python'
>>> c.strip()
'Hello Python'
>>> c.lstrip()
'Hello Python'
>>> c='Hello Python'
>>> c.lstrip()
'Hello Python'
>>> c='  Hello Python   '
>>> c.lstrip()
'Hello Python   '
>>> c.rstrip()
'  Hello Python'
>>> c.strip()
'Hello Python'
>>> text="Hello नमस्ते你好 café 🙂"
>>> text.encode()
b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
>>> b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'.decode()
'Hello नमस्ते你好 café 🙂'
>>> text="Hello नमस्ते 你好 café 🙂"
>>> text.encode()
b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
>>> b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'.decode()
'Hello नमस्ते 你好 café 🙂'
