# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.
import math
a = float(input("nhập độ dài cạnh a"))
b = float(input("nhập độ dài cạnh b"))
c = float(input("nhập độ dài cạnh c"))
def kiem_tra_tam_giac(a, b, c):
  
  # Kiểm tra điều kiện để a, b, c là ba cạnh của tam giác
  if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Không phải là ba cạnh của tam giác")

  # Kiểm tra các loại tam giác
  if a == b == c:
    print( "Tam giác đều")
  elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    if a == b or a == c or b == c:
      print( "Tam giác vuông cân")
    else:
      print("Tam giác vuông")
  elif a == b or a == c or b == c:
    print( "Tam giác cân")
  else:
    print("Tam giác thường")
    
ket_qua = kiem_tra_tam_giac(a, b,  c)
print(ket_qua)



#bài 8
import math 
diem = str(input("nhập điểm vào đây"))

if diem == "A":
    print("sinh viên loại suất sắc")
elif diem == "B":
    print("sinh viên loại giỏi")
elif diem == "C":
    print("sinh viên loại khá")
elif diem == "D":
    print("sinh viên loại trung bình")
elif diem == "E":
    print("sinh viên loại yếu")
else:
    print("sinh viển loại kém")
    
    
#bài 10
import math
luong = float(input("nhập mức lương của nhân viên vào đây(triệu đồng)"))
if luong >= 15:
    thue = luong*0.3
    luong_rong = luong - thue
    print(f"thue thu nhap la: {thue:.2f} triệu đồng")
    print(f"lương ròng là:{luong_rong:.2f} trieu đồng")
elif luong >= 7 and luong < 15:
    thue = luong*0.2
    luong_rong = luong - thue
    print(f"thue thu nhap la: {thue:.2f} triệu đồng")
    print(f"lương ròng là:{luong_rong:.2f} trieu đồng")
else:
    thue = luong*0.1
    luong_rong = luong - thue
    print(f"thue thu nhap la: {thue:.2f} triệu đồng")
    print(f"lương ròng là:{luong_rong:.2f} trieu đồng")
    
    
#bài 6
import math 

def menu_phim():
  print("Chào mừng đến với rạp chiếu phim ABC!")
  print("Vui lòng chọn thể loại phim bạn muốn xem:")
  print("1. Phim tình cảm")
  print("2. Phim kinh dị")
  print("3. Phim hoạt hình")
  print("4. Phim khoa học viễn tưởng")

  while True:
    try:
      lua_chon = int(input("Nhập lựa chọn của bạn (1-4): "))
      if 1 <= lua_chon <= 4:
        break
      else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
      print("Vui lòng nhập số!")

  # Thực hiện các hành động tương ứng với lựa chọn
  if lua_chon == 1:
    print("Bạn đã chọn phim tình cảm.")
  elif lua_chon == 2:
    print("Bạn đã chọn phim kinh dị.")
  elif lua_chon == 3:
    print("Bạn đã chọn phim hoạt hình.")
  else:
    print("Bạn đã chọn phim khoa học viễn tưởng.")

# Gọi hàm để hiển thị menu
menu_phim()

#bài 3
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    print("a là số lớn nhất")
    
elif b >= a and b >= c:
    print("b là số lớn nhất")
    
else:
    print("c là số lớn nhất")
    
#bài 2
x = float(input("Nhập hoành độ của điểm M: "))
y = float(input("Nhập tung độ của điểm M: "))
a = float(input("Nhập hoành độ của tâm I: "))
b = float(input("Nhập tung độ của tâm I: "))
R = float(input("Nhập bán kính của hình tròn: "))
# khoảng cách từ M đến I
khoang_cach = math.sqrt((x - a)**2 + (y - b)**2)
if khoang_cach <= R:
    print("điểm M nằm trên hoặc trong dường tròn")
    print("True")
else:
    print("điểm M nằm ngoài đường tròn")
    print("False")
    
# bài 9
import  math
loai_xe = int(input("Nhập loại xe (4 hoặc 7 chỗ): "))
quang_duong = float(input("Nhập quãng đường (km): "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))
