import re

l1=[8,5,3,7,4,1005,-505,9,55,8,65,-11,-55]
l2=[]
max=l1[0]
for each in range(1,len(l1)):
    if l1[each]>max:
        max=l1[each]
        l2.append(max)
print(max)
print(l2)

min=l1[0]
for each in l1:
    if each<min:
        min=each
print(min)
temp=0

regex="[0-9]{3}"+"."+"[0-9]{3}"+"."+"[0-9]{1,3}"+"."+"[0-9]*"
r="192.16.0.12"
s=re.search(regex,r)
print(s)

aadhar="[1-9]{4}"+"\s"+"[0-9]{4}"+"\s"+"[1-9]{4}"
a="123 7878 7867"
p=re.search(aadhar,a)
print(p)

url="[http:|https:]"+"//"+["www."]


