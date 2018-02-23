a=raw_input()
n=len(a)
p=0
q=0
for i in range(0,n):
  if(a[i]>='a' and a[i]<='z'):
    p+=1
  if(a[i]>='0' and a[i]<='9'):
    q+=1
if((p and q)>1):  
  print("yes")
else:
  print("no")
