'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):

     num, m, c = input().split()

     num, m = int(num), int(m)

     binary = bin(num)[2:].zfill(16)

     if c=='R':

          binary = binary[-m:]+binary[:-m]

     else:

          binary = binary[m:]+binary[:m]

     print(int(binary,2))