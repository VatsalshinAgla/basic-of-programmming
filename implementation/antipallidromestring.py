'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
T = int(input())

for i in range(T):

   #check for palindrome

   my_str = input()

   if my_str == my_str[::-1]:

       print("-1")

   else:

       print(''.join(sorted(my_str)))