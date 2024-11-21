print("hello world")

a = "hello world"
b = "hello world"

c = 'ban A noi :"abc"'
d = ' ban a noi: "abc"'

# kiểu dữ liệu tuần tự là kiểu dữ liệu có thể truy cập vào phàn tử trong nó 
# truy cập sử dụng index ( danh mục)

print(a[4])

# [start:stop:step]
# start : vị trí bắt đầu 
# stop :  vị trid kết thúc
#step: khoảng cách giữa các bước
print(a[1:7]) #  lấy các giá trị từ start đến stop-1
# print(a[:7])
# print(a[1:])
# print(a[:])
# mặc định của step = 1
print(a[1:7:2])
print(a[:7:2])
print(a[1::2])
print(a[::2])
print(a[::])
print(a[::-1])

print(range(5)) # 0,1,2,3,4
# range cũng sử dụng start , stop, step
range(1,5)
range(1,5,2)


for item in a :
    print(item)

# hàm đo độ dài kiểu dữ liệu tuần tự : len 
print(len(a))
range(len(a)) #thu được chỉ mục chạy từ 0 đến len(a)-1 = 10
for i in range(len(a)):
    print(a[i])
    
# tính chất của kiểu dữ liệu ký tự:
# - có thể truy cập 
# - không thêr chỉnh sửa 
# - không thể sắp xếp  
b = "hello " + "world"
print(b)

n = int(input("nhap vao so nguyen duong:"))
if n >0:
    print("nhap vào so nguye duong")
      
c = ""
for i in range(len(a)):
    if a[i] == "a":
        c = c + i
# for i in a:
#     print(j)      
# các phương thức trong xử lý chuối ký tự 
a = "Hello world"
# các phương thức kiểm tra ( trả vể cho mình true hoặc false)
# các phương thức kiểm tra này sẽ thường bắt đầu băngf chữ "is"

# - kiểm tra  chuỗi có phải alphanumeric (chỉ có ký tự số và chữ hay không)
# print(a.isalnum())  
# - kiểm tra chuỗi có toàn sôs hay không(numeric)
# print(a.isnumeric())
# - kiểm tra xem chuỗi có toàn chữ  hay không ( character)
# print(a.isalpha)
# - kiểm tra chuỗi có nằm trong bảng mã ascii hay không
# print(a.isascii())
# - kiểm tra chuỗi có phải kiểu số hay không 
# a = "123"
# print(a.isdigit()) # số thông thường
        
# print(a.isdecimal())# số thập phân

a = "Hello world"
# - kiểm tra xem chuỗi có khoảng trống hay không
# print(a.isspace())
# - kiểm tra in hoa in thường 
# print(a.isupper())
# print(a.islower())
a = "hello world "
# - kiểm tra kí tự tồn tại trong chuỗi
# print(a.find("llo"))
# print(a.count("l"))
# print(a.index("l"))


# phương thức biến đổi ( các phương thức này trả về chuỗi ký tự mới , không thay đổi chuỗi ký tự )
a = "hello world"
# xóa ký tự đầu và cuối của chuỗi
a.strip()
a.lstrip()
a.rstrip()

# - thay thế ký tự bất kỳ
a_sua = a.replace("l","w")

# - biến đổi viết hoa viết thường
a_sua = a.upper()
a_sua = a.lower()
a_sua = a.capitalize()
