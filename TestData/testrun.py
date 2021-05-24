a1=[1,1,2,3,0,0,8,5]
l=len(a1)
for i in range(0,l):
    if a1[i]==0:
       if a1[i+1]==0 and a1[i+2]==7:
           print("Yes values {},{},{} are present".format(0,0,7))
           break
       else:
            print("Yes values {},{},{} are not present".format(0, 0, 7))
            break






