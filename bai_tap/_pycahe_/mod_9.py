def ucln_dequy(a, b):
  """Tính ước chung lớn nhất bằng đệ quy"""
  if b == 0:
    return a
  return ucln_dequy(b, a % b)

def toi_gian_phan_so(tu_so, mau_so):
  """Hàm tối giản phân số sử dụng đệ quy"""
  uc = ucln_dequy(tu_so, mau_so)
  return tu_so // uc, mau_so // uc

# Ví dụ sử dụng hàm
tu_so = 66
mau_so = 18
tu_so_toi_gian, mau_so_toi_gian = toi_gian_phan_so(tu_so, mau_so)
print(f"{tu_so}/{mau_so} tối giản thành {tu_so_toi_gian}/{mau_so_toi_gian}")
