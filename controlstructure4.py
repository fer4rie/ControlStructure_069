# 4. Write a PYTHON program to print odd numbers up to n!

n = int(input("Enter n to print odd numbers up to n: "))

print("Odd numbers up to", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end= " ")
print()