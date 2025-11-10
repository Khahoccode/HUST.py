#Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, 
# kiểm tra xem đó là tam giác gì
#  (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)


a = float(input("Nhap vao so a: " + " "))
b = float(input("Nhap vao so b:" + " "))
c = float(input("Nhap vao so c:" + " "))

if (a + b > c) and (a+c>b) and (b+c>a):
    if (a == b == c): 
        print("Tam giac deu") 
    elif(a == b or a==c or b==c): 
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2): 
            print("Tam giac vuong can")
        else: 
            print("Tam giac can")
    elif(a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2): 
            print("Tam giac vuong")
    else: 
         print("Tam giac thuong")
else:
        print("Khong phai la mot tam giac")

