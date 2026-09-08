import re
'''text='Codegnan'
pattern=r'Code'
res=re.match(text,pattern)
print(res.group() if res else "Pattern not found.")

pattern = r'[0-9]'
text = 'codegnan2026'
res = re.search(pattern,text)
print(res.group() if res else "Pattern not found")

pattern=r'[0-9]'
text='Codegnan 2026 python version 3.14'
res=re.findall(pattern,text)
print(res)

pattern=r'[0-9]'
text='Codegnan 2026 python version 3.14'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
    
pattern=r'[0-9]{10}'
text='9856321470'
res=re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not found")

pattern=r'[,(#)]'
text='java,python,(html#css)'
res=re.split(pattern,text)
print(res)

pattern=r'[0-9]'
text='python version 3.14, batch-63'
res=re.sub(pattern,'*',text)
print(res)

pattern=r'e.t'
text='e@t eaat eat eet ett ect Egfhjet hgjeokj'
res=re.findall(pattern,text)
print(res)

pattern=r'^(91)'
text='91987582310'
res=re.findall(pattern,text)
print(res)

pattern=r'0$'
text='91987582310'
res=re.findall(pattern,text)
print(res)

pattern=r'to+'
text='to tdfghjk too tooo toooooo'
res=re.findall(pattern,text)
print(res)

pattern=r'ab++'
text='ab abbb a abbbbb abbbbbb'
res=re.findall(pattern,text)
print(res)

pattern=r'91|0'
text='05678'
res=re.findall(pattern,text)
print(res)'''

pattern=r'[aeiouAEIOU]'
text='Codegnan programming'
res=re.findall(pattern,text)
print(res)