# khởi tạo 1 danh sách
# a = []
# b = ["abc",1 5 ,6.7,[]]

# a = 5
# b = a
# b = a + 1
# print(a)
# print(b)

# # bộ nhớ list được chia sẻ cho nhau
# a = ["abc","bef","ghijk",1 ,2 ,3 ]
# b = a
# b[0] = "chuoi thay doi"
# print(a)
# print(b)


# phương thức sao lưu 
a = ["abc","bef","ghijk",1 ,2 ,3 ]
b = a.copy()
print(a)
print(b)

# # thay đổi giá trij trong danh sách 
a = ["abc","bef","ghijk",1 ,2 ,3 ]
# a[3] = 10
# a[1:4] = [6,7,8]
# print(a)
# # độ daif của danh sách 
print(len(a))
# các phương thức 
# phương thưcs thêm và bót 
#thêm cuối danh sách 
a.append("abca")
a.append([])
print(a)
# thêm nhiều phần tử vào danh sách 
a.extend([1,2,3])
print(a)
# xóa các phần tử trong danh sách 
a.clear()
#lấy phần tử cuối cungf ra khỏi danh sách sử dụng
b = a.pop()
print(a)
print(b)
# xóa 1 phần tử trong chuỗi

a.remove("abc")
# thêm 1 phần tử vào vị trí index
a.insert(3, "kkk")

# đếm số phân tử xuất hiện
a.count("abc")
# đảo ngược danh sách
a.reverse()
# trả về vị trí xuất hiện đầu tiên của phần tử trong danh sách
a.index()
# sắp xếp danh sách

a.sort(revers=True)
# a.sort(key=)

b = [[1,2,[4,5,6]],"abc",[3,"rts",5]]
print(b[0][2][1])

# bài tập xử lý ma trận
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
# nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n
print(matrix_a)

# yêu cầu về nhà 
# thực hiện các phep stinhs cơ bản        