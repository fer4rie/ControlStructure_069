# 3. Write a PYTHON program to print Fibonacci series up to n!

n = int(input("Enter number by using fibonacci series up to n: "))

a, b = 0, 1
count = 0
print("Here's the answer to the Fibonacci series up to", n, ":")

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1  #using fibonacci series up to n