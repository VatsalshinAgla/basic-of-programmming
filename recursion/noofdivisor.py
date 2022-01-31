'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for _ in range(int(input())):

    n, k = [int(i) for i in input().split()]

    x=0

    while n!=0:

        q = n // k

        x += (((n * (n + 1)) // 2) - ((q * (q + 1)) // 2) * k)

        n = q

    print(x)