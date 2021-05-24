l1=[5,6,8,3,2,8,1]
for one in range(len(l1)):
    for two in range(one+1,len(l1)):
        if l1[one]>l1[two]:
            temp=l1[two]
            l1[two]=l1[one]
            l1[one]=temp
print(l1)

l1=[5,6,8,3,2,8,1]
for each in range(1,len(l1)):
    for y in range(0,each):
        if l1[each]>l1[y]:
            print(l1[y])

l3="((())"
l4="{}[("
l5="([{]})"

def brackets(num):
    a = "{}"
    b = "[]"
    c = "()"
    if len(a) not in range(2,50,2):
        print("Not correct")
    else:
        print("validation entered")
        for i in range(len(l4)):
            if a[0] in l4 and a[1] in l4:
                x=l4.index(a[0])
                y=l4.index(a[1])
                print(x,y)
                assert y>x








y=brackets(l4)
print(y)
