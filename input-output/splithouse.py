'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

2

n=int(input())

s=input()

if 'HH' in s:

    print('NO')

else:

    s=s.replace('.','B')

    print('YES')

print(s)