# cau lenh dieu kien 
# 3 kieu viet cau lenh diều kiện 
# câu lệnh if ..( sử dụng 1 điều kiện để xét)
# câu lệnh if ... else..(sử dụng 1 điều kiện để xét và có điều kiện khác)
# câu lệnh if ....elif ...else (sử dụng mhieeuf điều kiện còn xét)

# xử lý xoay quanh bôlean (true false)
1 > 2
1 < 2

1 <= 2
1 == 2
1 != 2
"abc" == "123"
#=> trả về kết quả true hoặc false
# đói với if thì xét điều kiện 
# - nếu điều kiện đúng (true) thì câu lệnh if sẽ hoạt động 
# - nếu điều kiện sai (false) thì câu lệnh if sẽ bị bỏ qua
a = 10
if a > 5:
    print("gia tri a thoa man dieu kien")
    b = a + 1
    
print("ket thuc chuong trinh")
# đói với câu lệnh if ...else khi xét điều kiện 
# nếu điều kiện đúng (tue) thì câu lệnh của if sẽ hoạt động 
# nếu điều kiện sai (false) thì câu lệnh else sẽ phản hồi 

# dối với câu lệnh if ...elif .. else
# nếu điều kiện của if đúng thì câu lệnh if se hoạt động 
# nếu câu điều kiện if sai thì xét tiếp điều kiện của elif
  # nêú dk của elif sai thì câu lệnh else hoạt động 
  # nếu dk của elif dúng thì cau lenh elif hoạt đọng 

a = 0
if a > 0:
    print("a la so duong")
elif a < 0:
    print("a la so am")
else:
    print("a la so 0")
print("ket thuc chuong trinh")
 # co bao nhiêu elif cũng được nhưng chỉ có 1 if và 1 else
 
#x thuoc khoang (2, 8) hợp (14, 24)
#and và 
#or hoặc

c = 1
(c > 2 and c <= 8) #(2, 8)
(c >= 14 and c < 24) #(14, 24)
 
 

(c > 2 and c <= 8) or (c >= 14 and c < 24)  #(2, 8) hợp 
