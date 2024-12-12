def tinh_tich(danh_sach_so):
    tich = 1  # Khởi tạo giá trị ban đầu của tích
    for so in danh_sach_so:
        tich *= so  # Nhân từng phần tử vào tích
    return tich

# Ví dụ sử dụng
danh_sach_so = [1, 2, 3, 4, 5]
kq = tinh_tich(danh_sach_so)
print(f"Tích của dãy số là: {kq}")