#Câu lệnh điều kiện
#3 kiểu viết câu lệnh điều kiện
#câu lệnh if... (sử dụng với 1 điều kiện xét)
#câu lệnh if...else... (sử dụng với 1 điều kiện xét và có điều kiện phủ định)
#câu lệnh if...elif...else (sử dụng với nhiều điều kiện cần xét, thứ tự điều kiện xét từ trên xuống dưới và có điều kiện phủ định)

#xử lý xoay quanh boolean (True, False)
1 > 2
1 < 2
1 >= 2
1 <= 2
1 == 2
1 != 2
"abc" == "123"
#=> trả về kết quả True hoặc False
#Đối với if khi xét điều kiện
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện sai (False) thì câu lệnh của if sẽ bị bỏ qua
a = 10
if a > 20:
    print("Gia tri a thoa man dieu kien")
    b = a + 1

print("Ket thuc chuong trinh")

#Đối với if...else khi xét điều kiện
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện sai (False) thì câu lênh của else sẽ được phép hoạt động
a = 10
if a > 20:
    print("Gia tri a thoa man")
else:
    print("Gia tri a khong thoa man")

print("Ket thuc chuong trinh")

#Đối với if...elif...else:
# - Nếu điều kiện của if đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện của if sai (Flase) thì xét tiếp điều kiện của elif
#       + Nếu điều kiện của elif đúng (True) thì câu lệnh của elif hoạt động
#       + Nếu điều kiện của elif sai (False) thì câu lệnh else sẽ hoạt động

a = 0
if a > 0:
    print("a la so duong")
elif a < 0:
    print("a la so am")
elif a < 0:
    print("a la so am")
elif a < 0:
    print("a la so am")
elif a < 0:
    print("a la so am")
elif a < 0:
    print("a la so am")
elif a < 0:
    print("a la so am")
elif a < 0:
    print("a la so am")
else:
    print("a la so 0")
    
print("Ket thuc chuong trinh")


#x thuoc khoang (2, 8] hop [14, 24)
#and (và)
#or (hoặc)

c = 1
(c > 2 and c <= 8) #(2, 8]
(c >= 14 and c < 24) #[14, 24)

(c > 2 and c <= 8) or (c >= 14 and c < 24) # (2, 8] hop [14, 24)
if (c > 2 and c <= 8) or (c >= 14 and c < 24):
    print("Thoa man dieu kien")
    

if c > 2 and c <= 8:
    print("Thoa man dieu kien")
elif c >= 14 and c < 24:
    print("Thoa man dieu kien")
else:
    print("dieu kien khong thoa man")
    
    
#Bài 1:
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nhap vao chieu cao: "))
if h> 0 and r > 0:
    pi = 3.14
    dtxq = 2*pi*r*h
    dttp = dtxq + 2*pi*r**2
    print(f"Dien tich xung quanh: {dtxq:.2f}")
    print(f"Dien tich toan phan: {dttp:.2f}")
else:
    print("gia tri nhap khong thoa man")

print("ket thuc chuong trinh")