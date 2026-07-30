Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,3,2,4,5,64,3]
l
[1, 3, 2, 4, 5, 64, 3]
l=[2,1,4,3,2,4,2,3]
l
[2, 1, 4, 3, 2, 4, 2, 3]
l=[2,1,4,3,2,4,2,3]
l=[1,3,2,4,5,64,3]
id(l)
1522045901440
l.append(12)
l
[1, 3, 2, 4, 5, 64, 3, 12]
id(1)
140729553417000
l.append(14)
l
[1, 3, 2, 4, 5, 64, 3, 12, 14]
id(l)
1522045901440
l.insert(1,13)
l
[1, 13, 3, 2, 4, 5, 64, 3, 12, 14]
l.extend([52,34,21])
l
[1, 13, 3, 2, 4, 5, 64, 3, 12, 14, 52, 34, 21]
id(l)
1522045901440
l[3]
2
l.pop(52)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l.pop(52)
IndexError: pop index out of range
l.pop(5)
5
l.pop()
21
l,pop(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l,pop(2)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
l.pop(2)
3
l.remove(13)
l
[1, 2, 4, 64, 3, 12, 14, 52, 34]
del l[4]
l
[1, 2, 4, 64, 12, 14, 52, 34]
l.clear()
l
[]
l=[1,3,2,4,5,64,3]
max(l)
64
min(l)
1
sorted(l)
[1, 2, 3, 3, 4, 5, 64]
l
[1, 3, 2, 4, 5, 64, 3]
l.reverse()
l
[3, 64, 5, 4, 2, 3, 1]
l.sort()
l
[1, 2, 3, 3, 4, 5, 64]
l.sort(reverse=True)
>>> l
[64, 5, 4, 3, 3, 2, 1]
>>> sum(l)
82
>>> l=[1,4,5]
>>> m=[4,7,8]
>>> l
[1, 4, 5]
>>> 
>>> m
[4, 7, 8]
>>> m.append(10)
>>> m
[4, 7, 8, 10]
>>> l
[1, 4, 5]
>>> all(p1,'',[],(),set(),{},False])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> all([1,'',[],(),set(),{},False])
False
>>> any([1,'',[],(),set(),{},False])
True
>>> l.index(2)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l.index(2)
ValueError: 2 is not in list
>>> l
[1, 4, 5]
>>> l.count(5)
1
>>> l.count(4)
1
>>> l=[[1,2,3,4,5],[3,4,5,6,7]]
>>> l
[[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]]
>>> l[0]
[1, 2, 3, 4, 5]
>>> l[1]
[3, 4, 5, 6, 7]
>>> l[0][2]
3
>>> l[1][3]
6
>>> l[-1][-1]
7
