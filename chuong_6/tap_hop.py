# #set - tập hợp trong python
# # tính chất của tập hợp 
# #-không có sắp xếp , không có thức tự
# #- những phần tử trong tập hợp là dặc hiệu (unique)
# #- các giá trị trong set có thể thay đổi được tuy nhiên nó chỉ có thể chứa các phần tử mang giá trị ko dổi
# list_a = ["fol","baa","baal"]

# set_a = {1,2,3,"abc"}
# set_b = set(list_a)#=> {"fol","baa","baal"}

# # kiểm tra số phần tử trong tập hợp 
# len(set_a)

# # kiểm tra phàn tử có tồn tại trong tập hợp không 
# 2 in set_a #=> trả về kiểu dữ liệu boolean : True

# if 2 in set_a:
#     print("2 co trong tap hop")
    
# 2 not in set_a #=> trả về kiểu dữ liệu boolean : false

# if 2 not in set_a:
#     print("2 khong co trong tap hop")
    
# # kiểm tra so sánh 2 tập hợp 
# # tập hợp A
# tap_hop_a = {"a","b","c","d"}
# # tập hơpj B
# tap_hop_b = {1,2,3,"a","b"}

# # kiểm tra tập A có phải tập con của tập B không ?
# tap_hop_a.issubset(tap_hop_b)#=> trả về  kiểu dữ liệu boolean
# tap_hop_a < tap_hop_b
# tap_hop_a <= tap_hop_b 

# # kiểm tra tập hợp A có phải tập hợp cha của tập hợp B không 
# tap_hop_a.issuperset(tap_hop_b)
# tap_hop_a > tap_hop_b
# tap_hop_a >= tap_hop_b 

# # kiểm tra xem 2 tập họp có giao nhau hay không
# tap_hop_a.isdisjoint(tap_hop_b)#=> trả vê True nuếu không có phần tử chung > trả về False nêus co phàn tử chung

# # tập hợp A
# tap_hop_a = {"a","b","c","d"}
# # tập hơpj B
# tap_hop_b = {1,2,3,"a","b"}
# # tập hợp C
# tap_hop_c = {1,2,3,4,5,6}
# # phép hợp tap hợp 
# tap_hop_tong = tap_hop_a.union(tap_hop_b)
# tap_hop_tong = tap_hop_a.union(tap_hop_b).union(tap_hop_c)
# tap_hop_tong = tap_hop_a | tap_hop_b | tap_hop_c

# # phép lấy giao giữa các tập hợp
# tap_hop_giao = tap_hop_a.intersection(tap_hop_b)
# tap_hop_giao = tap_hop_a.intersection(tap_hop_b).intersection(tap_hop_c)
# tap_hop_giao = tap_hop_a & tap_hop_b & tap_hop_c

# # phép lấy phàn tử  trong  1 tập hợp mà không có trong các tập hợp còn lại
# tap_hop_khac = tap_hop_a.difference(tap_hop_b)
# tap_hop_khac = tap_hop_a.difference(tap_hop_b).difference(tap_hop_c)
# tap_hop_khac = tap_hop_a - tap_hop_b - tap_hop_c

# # phép lấy các phần tử có trong tập hợp này mà không có trong tập hợp khác
# tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b)
# tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b).symmetric_difference(tap_hop_c)
# tap_hop_khac_giao = tap_hop_a ^ tap_hop_b ^ tap_hop_c 

# # chỉnh sửa tập hợp
# tap_hop_a = {1,2,3 ,"a"}
# tap_hop_b = {"a","b","c"}
# # thêm phần tử vào a
# tap_hop_a.add(9)
# tap_hop_a.update([4,5,6]) # tương tự với việc hợp 2 tập hợp
# # a = 1 
# # b = 2
# # a += b
# # a = a+ b
# tap_hop_a = tap_hop_a | tap_hop_b 
# tap_hop_a |= tap_hop_b 

# # giữ lại các phần tử là giao của các phần tử  
# tap_hop_a.intersection_update(tap_hop_b)
# tap_hop_a = tap_hop_a & tap_hop_b
# tap_hop_a &= tap_hop_b

# # giữ lại các phần tử có trong tập xét mà khôg có  trong tập hợp còn lại 
# tap_hop_a.difference_update(tap_hop_b)
# tap_hop_a = tap_hop_a - tap_hop_b
# tap_hop_a -= tap_hop_b 

# # giữ lại các phần tử không có trong cả 2 tập hơpkj
# tap_hop_a.symmetric_difference_update(tap_hop_b)
# tap_hop_a = tap_hop_a ^ tap_hop_b
# tap_hop_a ^= tap_hop_b 

# # xóa phần tử trong tập hợp
# # xóa 1 phần tử 
# tap_hop_a.remove(2)
# # xóa nhiều phần tử tronh 1 tập hợp 
# tap_hop_a.difference_update({1,2})
# # xóa phần tử không gây lỗi
# tap_hop_a.discard(2)
# # lấy 1 phần tử bất kì ra đẻ sử dụng và xóa phàn tử này khỏi tập hợp 
# tap_hop_a.pop()
# # xóa toàn bộ tập hợp
# tap_hop_a.clear()

tap_hop = {"a","b","c","d","e"}
while tap_hop:
    a = tap_hop.pop()
    print(a)

