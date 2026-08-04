Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=set()
s={1,2,3,5,6,4,7,8,9,25,36}
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 36, 25}
type(S)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
type(s)
<class 'set'>
s=set()
s
set()
s.add(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.add(a)
NameError: name 'a' is not defined
s.add(1)
s.add(12.3)
s.add(2+4j)
s
{1, 12.3, (2+4j)}
s={1,1,1,1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
{1}<=a
True


#{1}{2}{3}{4}{5}{1,2}{2,3}{3,4}{1,4}{1,2,3,4}
{1}<=a
True
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.isunion(b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.isunion(b)
AttributeError: 'set' object has no attribute 'isunion'. Did you mean: 'union'?
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.superset(b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c
{1, 2, 3, 4, 5, 12}
c.add
<built-in method add of set object at 0x0000014333A07D80>
c.add(13)
b
{1, 2, 3, 4, 5, 12}
c
{1, 2, 3, 4, 5, 12, 13}
a.discard(12)
a.discard(5)
q
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    q
NameError: name 'q' is not defined
a
{1, 2, 3, 4}
a.clear()
a
set()
a={1,2,3,4,5,12}
a
{1, 2, 3, 4, 5, 12}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
1
a.pop()
2
a.pop()
3
a.remove(16)
a
{4, 5, 12, 17, 18, 123}
a.remove(12)
a
{4, 5, 17, 18, 123}
a.clear()
a
set()
a={1,2,3,4,5}
a.update({"str",0,12,13,-1,-23.4})
a
{0, 1, 2, 3, 4, 5, -23.4, 12, 13, 'str', -1}
len(a)
11
all(a)
False
any(a)
True
a=frozenset({1,12,13,10,18,59,20})
a
frozenset({1, 18, 20, 10, 59, 12, 13})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
1388097977920
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
1388097977920
d={}
d[1]='int'
d
{1: 'int'}
>>> d[12.3]='flt'
>>> d
{1: 'int', 12.3: 'flt'}
>>> d[2+6j]='com'
>>> d
{1: 'int', 12.3: 'flt', (2+6j): 'com'}
>>> d['str']='string'
>>> d
{1: 'int', 12.3: 'flt', (2+6j): 'com', 'str': 'string'}
>>> d[(1,2,3,4)]='tuple'
>>> d
{1: 'int', 12.3: 'flt', (2+6j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
>>> d={}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]=3+90j
>>> d[4]='Moksha'
>>> d[5]=[1,2,3,4,3]
>>> d[6]=(3,4,5,6)
>>> d[7]={1,2,3}
>>> d[8]={1:4}
>>> d
{1: 1, 2: 12.3, 3: (3+90j), 4: 'Moksha', 5: [1, 2, 3, 4, 3], 6: (3, 4, 5, 6), 7: {1, 2, 3}, 8: {1: 4}}
>>> 9 in d
False
>>> 8 in d
True
>>> 'Moksha' in d
False
>>> d[5]
[1, 2, 3, 4, 3]
>>> d[8]
{1: 4}
>>> d
{1: 1, 2: 12.3, 3: (3+90j), 4: 'Moksha', 5: [1, 2, 3, 4, 3], 6: (3, 4, 5, 6), 7: {1, 2, 3}, 8: {1: 4}}
>>> d[3]=4
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'Moksha', 5: [1, 2, 3, 4, 3], 6: (3, 4, 5, 6), 7: {1, 2, 3}, 8: {1: 4}}
>>> d[5]=190
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'Moksha', 5: 190, 6: (3, 4, 5, 6), 7: {1, 2, 3}, 8: {1: 4}}
>>> d[6]=12
>>> d[7]=[1,2,3,4,5,67]
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'Moksha', 5: 190, 6: 12, 7: [1, 2, 3, 4, 5, 67], 8: {1: 4}}
