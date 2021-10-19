'''
s='juber'
r=reversed(s)
j=''.join(r)
print(j)

s='jubermulla'
i=len(s)-1
output=''
while i >=0:
    output = output + s[i]
    i=i-1
print(output)

n=50
i=0
while i<n:
    i+=1
    print(i)

n=50
i=0
while True:
    i+=1
    print(i)
    if i==50:
        break

s='juber nasaruddin mulla'
j=s.split()
l=j[::-1]
print(' '.join(l))

s='juber nasaruddin mulla'
for i in reversed(s.split()):
    print(i,end=' ')

s='juber nasaruddin mulla'
j=s.split()
i=len(j)-1
output=''
while i>0:
    output = output + s[j]
    i=i-1

print(output)

s='juber nasaruddin mulla'
l=s.split()
l1=[]
for i in l:
    l1.append(i[::-1])
print(l1)

s='one two three four five six'
j=s.split()
i=0
list=[]
while i < len(j):
    if i%2==0:
        list.append(j[i])
    else:
        list.append(j[i][::-1])
    i=i+1
print(list)

s='jubermulla'
i=1
output=''
while i<len(s):
    output=output+s[i]
    i=i+2
print(output)

s='a4b3c2'
alphabet=[]
digit=[]
for i in s:
    if i.isnumeric():
        alphabet.append(s[i])
    else:
        digit.append(s[i])
print(alphabet+digit)

s='juberj'
d={}
for i in  s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

s='one two three four five six'
j=s.split()
i=0
list=[]
while i < len(j):
    if i%2==0:
        list.append(j[i])
    else:
        list.append(j[i][::-1])
    i=i+1
print(list)

s='one two three four five six'
#output=one,owt,three,ruof,five,xis
j=s.split()
l=[]
for i in range(len(j)):
    if i%2==0:
        l.append(j[i])
    else:
        l.append(j[i][::-1])
print(l)

j='jubbebrjlj'
def display(j):
    chr=j[0]
    j=j.replace(chr,'$')
    j=chr+j[1:]
    return j
print(display(j))

def change_string(string):
    first_char=string[0]
    modified_string=string[1:].replace(first_char,'$')
    return first_char+modified_string
print(change_string('restrart'))

#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
j1,j2='abc','xyz'
new_j1=j2[:2]+j1[2:]
new_j2=j1[:2]+j2[2:]
output=new_j1+' '+new_j2
print(output)

#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
s='ab'
if len(s)>=3:
    if s[-3:]=='ing':
        s=s+'ly'
        print(s)
    else:
        s=s+'ing'
        print(s)
else:
    print(s)

s='hello python how are you'
str1='pythonj'
if (s.find(str1) ==-1):
    print('no substring')
else:
    print('substring is present')


j=s.split()
k=max(j)
print(k)
print(len(k))

s='juber nasaruddin mulla'
j=sorted(s.split())
print(j[-1])
print(len(j[-1]))

def longest_word(string):
    l=0
    w=''
    words=string.split()
    for i in words:
        if (len(i) >l):
            w=i
            l=len(i)
    return (w,l)
print(longest_word('juber nasaruddin mullabababjbj'))


a = 'hello'
b = 'welcome'
c = 'pune'

print(j)

a = 'hello'
b = 'welcome'
c = 'pune'
print(a,end=' ')
print(b,end=' ')
print(c,end=' ')

s= 'B4A1D3'
al=[]
di=[]
for i in s:
    if i.isalpha()==True:
        al.append(i)
    else:
        di.append(i)
output=''
for i in sorted(al):
    output=output+i
for j in sorted(di):
    output=output+j
print(output)
'''
