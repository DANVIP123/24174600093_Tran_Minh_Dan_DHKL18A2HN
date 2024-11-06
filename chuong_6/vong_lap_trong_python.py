#vòng lặp trong python
#vòng lặp có giới hạn( vòng lặp for)

#các kiểu dữ liệu tuần tự: string, list, tuple,set, dictionary
# range()
n = input()
for abc in range(10):
    print(abc)
#range(10) -> 0,1,2,3,4,5,6,7,8,9
#range khi truyền giá trị mặc định yêu cầu phải là giá trị nguyên dương
#các giá trị trong range sẽ chạy từ 0 -> n-1

#khi sử dụng vòng lặp nên kết hợp sử dụng với các câu lệnh điều kiện
#( khi sử dụng vòng lặp nên có mục đích rõ ràng)

# trong python vòng lặp cung cấp cho người dùng 3 công cụ : break , continue, else
# break : dừng vòng lặp ngay lập tức thoạt tại lần lặp gặp break
for i in range(10):
    if i == 4:
        break
    print(i)
        
# continue: vòng lặp sẽ bỏ qua lần lặp mà ở đây xuất hiện continue
for i in range(10):
    if i == 4:
        continue
    print(i)
        

# else: vòng lặp sẽ chạy các câu lệnh xử lý của else trong trường hợp 
#       vòng lặp không gặp break
for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("chạy cau lenh else")
    
#hoặc
for i in range(10):
    if i == 4:
        continue
    print(i)
else:
    print("chạy cau lenh else")
    
        
#vòng lặp không giới hạn( vòng while)
n = 10
while n >2: #luôn là  true
    print(f" chạy vòng lặp {n}")
    n = n - 1


# vong lap while cung ho tro : break , continue va else
# break 
n = 10
while n > 2:
    print(f"chạy vòng lặp {n}")
    n = n - 1
    if n == 6:
        break
    
# continue
n = 10
while n > 2:
    n = n - 1
    if n == 6:
        continue
    print(f"chạy vòng lặp {n}")
    
# else
n = 10
while n > 2:
    print(f"chạy vòng lặp {n}")
    n = n - 1
    if n == 6:
        continue
else:
    print(" chạy câu lệnh else")
    
# tìm số nguyên tố lớn nhất  nhỏ hơn hoặc bằng 20    
n = 20
while True:
    for i in range(1,n):
        if n%i == 0 and i !=  1 and i != n:
            n = n -  1
            print(" số này không phải là số nguyên tố ")
            break
    else:
        break  
    if n < 1:
        break
print(f"so nguyen to la {n}")
    
n = 20 
while True:
    for i in range(1,n):
        if n%i == 0 and i !=  1 and i != n:
            n = n -  1
            print(" số này không phải là số nguyên tố ")
            break
    else:
        break  
    if n < 1:
        break
print(f"so nguyen to la {n}")