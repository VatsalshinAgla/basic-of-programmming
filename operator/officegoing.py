'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
d=float(input())

oc,of,od=map(float,input().split())

cs,cb,cm,cd=map(float,input().split())

m = oc+(d-of)*od

a= cb+(d/cs)*cm+(d*cd)

if m<a:

    print('Online Taxi')

elif m==a:

    print('Online Taxi')

else:

    print('Classic Taxi')   