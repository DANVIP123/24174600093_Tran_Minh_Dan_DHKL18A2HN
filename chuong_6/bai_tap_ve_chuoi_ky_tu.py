# bài tập về chuỗi ký tự 
# dạng thứ nhất : áp dụng xử lý chuỗi ký tự bằng các phương thức có sẵn 
# bài 1 nhận vào một chuỗi ký tự bất kỳ . diếm số ký tự trong chuỗi 
#cách 1
chuoi_nhap_vao = input("nhap vao chuoi ky tu")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"so ky tu tring chuoi la{so_ky_tu_trong_chuoi}")
# cách 2
chuoi_nhap_vao = input("nhap vao chuoi bat ky:")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem = dem +1
print(f"so ky tu trong chuoi la {dem}")


# bài 2 nhập vào 1 chuỗi bất kỳ . xóa các khoảng trống ở đầu và cuối chuỗi
# cách 1
chuoi_nhap_vao = input("nhap vao chuoi bat ky:")
chuoi_sau_khi_xoa_khoang_trong = chuoi_nhap_vao.strip()
print(f"chuoi sau khi xoa khoang trong {chuoi_sau_khi_xoa_khoang_trong}")
#cách 2 "chu" ở dây là chữ
#"   chuoi nhap vao        "
chuoi_xu_ky_dau =""
kiem_tra_dau = False 
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu
# giảm 1 chuỗi
chuoi_dao_nguoc = chuoi_xu_ky_dau[::-1]
chuoi_dao_nguoc_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_dao_nguoc:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_dao_nguoc_xu_ly_dau = chuoi_dao_nguoc_xu_ly_dau + chu
chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"chuoi sau khi xoa khoang trong {chuoi_ket_qua}")

# bài 3 nhập vào 1 chuỗi bất kỳ . Xoá tất cả các khoảng trống trong 1 chuôĩ
# ví dụ "  chuoi  nhap     vao     "
# cách 1:
chuoi_nhap_vao = input("nhap vao chuoi bat ky :")
tach_chuoi = chuoi_nhap_vao.splip()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuoi nhap vao"
print(f"chuoi ket qua: {chuoi_ket_qua}")

# cách 2 bài tạp về nhà xử lý yêu câu trên mà không sử dụng các phương thức
nhap_chuoi_vao = input("nhap chuoi cua ban vao:")
bien_luu_tam = []
bien_hien_tai = ""
for chu in chuoi_nhap_vao:
    if chu != " ":
        bien_hien_tai += chu
    else:
        if bien_hien_tai != "":
            bien_luu_tam += [bien_hien_tai]
            bien_hien_tai =""
if bien_hien_tai != "":
    bien_luu_tam += bien_hien_tai
chuoi_ket_qua = " ".join(bien_hien_tai)
print(f"chuoi")                

# dạng tứ 2 : áp dụng kết hợp xử lý vòng lặp và xử lý chuỗi ký tự
# bai 1:nhập vào 1 chuỗi ký tự bất kỳ . dếm xem có bao nhiêu ký rự số , kí tư chữ và bao nhiêu ký tự dăc biệt
# isalpha(): kiểm tra chữ cái
# isdigit(): kiemtra ky rự sô
chuoi_nhap_vao = input("nhap vao chuoi bat ky")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu = dem_so +1
    else:
        if chu.isdigit() == True:
            dem_so = dem_so + 1
        else:
            dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1
            
print(f"so chu cai: {dem_chu}")   
print(f"so so;{dem_so}") 
print(f"so ky tu dac biet:{dem_ky_tu_dac_biet}")  

# bài 2 nhập vào 1 số bất kỳ , kiểm tra xem số này có phải là số nguyên tố hay không


            
                    


              