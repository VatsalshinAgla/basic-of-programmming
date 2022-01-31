count=0

l,r,k=map(int,input().split())

for item in range(l,r+1):

   if item%k==0:

       count+=1

   elif item%k!=0:

       pass  

print(count)