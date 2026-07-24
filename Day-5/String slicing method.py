Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String operations
>>> s='
SyntaxError: unterminated string literal (detected at line 1)
>>> s=''
>>> s
''
>>> s='mokshagna'
>>> s
'mokshagna'
>>> mokshagna+sai
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mokshagna+sai
NameError: name 'mokshagna' is not defined
>>> 'mokshagna'+'Sai'
'mokshagnaSai'
>>> 'mokshagna'*3
'mokshagnamokshagnamokshagna'
>>> '&$'*3
'&$&$&$'
>>> s='Mokshagna'
>>> s[5]
'a'
>>> s[0:9:-1]
''
>>> s[::-1]
'angahskoM'
>>> s[2:6:-1]
''
>>> s[-2:-6:-1]
'ngah'
>>> s[-2:-8]
''
>>> s[-8]
'o'
>>> s[-8:-5]
'oks'
>>> s[0:9:2]
'Mkhga'
>>> 'mok' in s
False
>>> 'Moks' in s
True
