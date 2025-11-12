a = int(input("Nhap vao so nguyen a: " + " "))
b = int(input("Nhap vao so nguyen b: " + " "))
for i in range (1,a+1):
    if i > b:
        break
    if a%i == 0 and b%i == 0:
        print(i)