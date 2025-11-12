# Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
a = int(input("Nhap vao so nguyen duong a: " + " "))
dem = 0;
for i in range (1, a+1):
    if(a%i==0):
        dem += 1
if dem == 2:
    print(str(a) + " la so nguyen to")
else:
    print(str(a) + " khong la snt")
