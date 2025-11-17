# Nhập vào số nguyên dương n, tính tổng các chữ số của n
n = int(input("Nhap vao so nguyen n: " + " "))
sum = 0
h = n
while h>0:
    a = h%10
    sum += a
    h = h // 10
print(sum)
