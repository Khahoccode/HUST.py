# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c 
# có cấu thành độ dài của 1 tam giác được không

a = float(input("Nhap vao so a: " + " "))
b = float(input("Nhap vao so b:" + " "))
c = float(input("Nhap vao so c:" + " "))

if (a + b > c) and (a+c>b) and (b+c>a):
    print ("a,b,c la do dai cua mot tam giac")
else:
    print ("a,b,c ko la do dai cua mot tam giac")

