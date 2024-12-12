def tinh_tong(day_so):
    """
    Hàm tính tổng của một dãy số nguyên bất kỳ.

    Tham số:
        day_so (list): Một danh sách chứa các số nguyên.

    Trả về:
        int: Tổng của dãy số.
    """
    tong = 0

    for so in day_so:
        tong += so

    return tong

# Ví dụ sử dụng

day_so = [1, 2, 3, 4, 5]
tong = tinh_tong(day_so)
print(f"Tổng: {tong}")