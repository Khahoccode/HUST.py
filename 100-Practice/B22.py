#Xet hoc luc cho hoc sinh
# Nhập điểm toán, văn, anh.

# Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:

# Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 
# và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
# Nếu không đủ điều kiện học sinh giỏi ta xét 
# nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 
# và không có điểm nào dưới 5 thì in ra “Học sinh khá”
# Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5,
# toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì
# in ra “Học sinh trung bình”
# Nếu không đủ điều kiện học sinh trung bình ta xét 
# nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 
# và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
# Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”

t = float(input("Nhap diem toan: " + " "))
v = float(input("Nhap diem van: " + " "))
a = float(input("Nhap diem anh: " + " "))

if (0 <= t <= 10 and 0 <= v <= 10 and 0 <= a <= 10):
    dtb = (t + v + a)/3
    if dtb >= 8 and (t >= 8 or v >=8 ) and (t >= 6.5 and v >= 6.5 and a >= 6.5):
        print("HS gioi")
    elif dtb >= 6.5 and (t>= 6.5 or v>=6.5) and (t>=5 and v>=5 and a>=5):
        print("HS kha")
    elif dtb >= 5 and (t>= 5 or v>= 5) and (t>=3.5 and v>=3.5 and a>=3.5):
        print("HS trung binh")
    elif dtb >= 3.5 and (t>= 3.5 or v>= 3.5) and (t>=2 and v>=2 and a>=2):
        print("HS yeu")
    else:
        print("HS kem")
else: print("Ban da nhap sai quy tac")