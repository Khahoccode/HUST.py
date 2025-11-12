# In toan bo uoc cua a
a = int(input("Nhap so nguyen duong a: " + " "))
print("Uoc cua a: ")
for i in range (1, a+1):
    if(a%i) == 0:
        print(i)