# Dem so uoc cua a
a = int(input("Nhap vao so nguyen a:" + " "))
r = 0
for i in range (1, a+1):
    if a%i == 0: 
        print(i)
        r += 1
print("So uoc cua a: ", r)
        