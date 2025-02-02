list1=[1,2,3,4,7,9]
#print(sum(list1))
total=0
for i in list1:
    #print(i)
    total=total+i
print(total)
#introducing condition
if total<=36:
    print('yes')
    total1=total*3
    print(total1)
else:
     total1=total+100
     print(total1)
     
     print('no')    

