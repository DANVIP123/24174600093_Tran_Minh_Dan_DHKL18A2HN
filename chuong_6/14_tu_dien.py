# từ điển trong python
#- lưu các kiểu dữ liệu khác nhau 
#- có thể thay đổi các giá trị trong từ điển 
#-có thể lưu các kiểu dữ kiệu tuần tự  khác tạo thành mạng lưới 
#- không thể sử dung chỉ mục mà thay vâo đó là các khóa (key)
# tất cả giá trị phải truy cập khóa 
tu_dien = {"abc":1,
           3:[1,2,3],
           (0,1):"hijk"}
# khai báo từ điển 
#- từ điển sử dụng ngoạc {} đẻ khởi tạo
#- mỗi phần tử phải theo cặp khóa : giá trị
# - khóa trong từ điẻne  phải là giá trị không thẻ thay đổi
#- khóa không được giống nhau
list_a = [(0, "hoang"), (1, "Cuong"),(2, "Lam")]
tu_dien_a = dict(list_a)
# từ điển trong python có cách hoạt động giống như JSON


# truy cập các phần tử trong từ điển 
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["a"]
# lấy tập hợp khoá
tap_hop_khoa = tu_dien.keys()
# lấy danh sách giá trị 
danh_sach_gia_tri = list(tu_dien.values())
# lấy danh sách các cặp khóa giá trị
danh_sach_khoa_gia_tri = list(tu_dien.items())

# thêm các giá trị vào trong từ điển
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["d"] = 4

tu_dien.update({"e": 5})
print(tu_dien)

# khóa phần tử trong từ điển
tu_dien.clear() # xóa toàn bộ các giá trị
tu_dien.pop("b") # lấy ra và xóa phần tử tại  khóa
tu_dien.popitem()# lấy ra và xóa phần tử bất kì