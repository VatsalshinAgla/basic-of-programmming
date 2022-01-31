'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):

   n = int(input())

   arr = set(map(int, input().split()))

   xor = 0

 

   for i in arr:

       xor ^= i

 

   for i in arr:

       temp = i ^ xor

       if temp not in arr:

           print(-1)

           break

   else:

       print(xor)

