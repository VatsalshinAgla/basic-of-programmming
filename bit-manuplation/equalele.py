'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())

m=int(input())

s=list(map(int,input().split()))

k=0

l=0

for i in s:


   if i%2==0:


       k+=1



   else:

       l+=1

if k<l:


   print(k)


else:


   print(l)