#In ra uoc chung lon nhat cua a va b
a =int(input("Nhap vao so nguyen a: " + " "))
b = int(input("Nhap vao so nguyen b: " + " "))
UCLN = 1
for i in range (1, a+1):
    if (a>b):
        break
    if (a%i ==0 and b%i==0):
        UCLN = i
print(UCLN)