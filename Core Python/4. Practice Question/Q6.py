import math
n = int(input("Enter a number: "))
num = n
sum_fact = 0

while n!=0:
    d = int(n%10)
    fact = math.factorial(d)
    sum_fact = sum_fact + fact
    n = n//10


if num == sum_fact:
    print ("Strong number")
else:
    print("Not a strong number")