# Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
n = int(input("Nhap n: " + " "))
n0 = n
while n % 2 == 0:
    n = n//2
if n == 1:
    print(str(n0) + " co dang 2^k")
else: 
    print(str(n0) + " khong co dang 2^k")




