
from math import gcd

def thap_phan_sang_phan_so(so_thap_phan):
    """
    Chuyển đổi một số thập phân thành phân số tối giản.

    Args:
        so_thap_phan (float): Số thập phân cần chuyển đổi.

    Returns:
        tuple: Một tuple (tu_so, mau_so) biểu diễn phân số tối giản.
    """
    # Xác định dấu của số thập phân
    dau = -1 if so_thap_phan < 0 else 1
    so_thap_phan = abs(so_thap_phan)

    # Chuyển đổi số thập phân thành chuỗi để phân tích phần thập phân
    so_chuoi = str(so_thap_phan)
    if '.' in so_chuoi:
        phan_nguyen, phan_thap_phan = so_chuoi.split('.')
        do_dai_thap_phan = len(phan_thap_phan)

        tu_so = int(phan_nguyen + phan_thap_phan)  # Tử số
        mau_so = 10 ** do_dai_thap_phan            # Mẫu số
    else:
        tu_so = int(so_thap_phan)
        mau_so = 1

    # Rút gọn phân số
    ucln = gcd(tu_so, mau_so)
    tu_so //= ucln
    mau_so //= ucln

    return (dau * tu_so, mau_so)

# Ví dụ sử dụng
if __name__ == "__main__":
    so_thap_phan = 0.75
    phan_so = thap_phan_sang_phan_so(so_thap_phan)
    print(f"Số thập phân {so_thap_phan} = Phân số {phan_so[0]}/{phan_so[1]}")


