#2. Write a PYTHON program to find largest of three numbers!!

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: " ))
c = float(input("Masukkan angka ketiga: "))

if a > b and a > c:
    largest = a
    print("Angka terbesar adalah:", largest)
elif b > a and b > c:
    largest = b
    print("Angka terbesar adalah:", largest)
elif c > a and c > b:
    largest = c
    print("Angka terbesar adalah:", largest)
else:
    print("Tidak ada angka terbesar")