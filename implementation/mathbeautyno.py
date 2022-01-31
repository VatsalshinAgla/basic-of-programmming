'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
tc = int(input())

for each in range(tc):

    x, k = map(int, input().split())

    flag = True

    while x > 0:

        if x % k >= 2:

            print("NO")

            flag=False

            break

        else:

            x = x//k

   

    if flag==True: print("YES")