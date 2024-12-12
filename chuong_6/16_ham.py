# def f():
#     s = '-- Inside f()'
#     print(s)
    
# print('Before calling f()')
# f()
# print('After calling f()') 
# def f(qty,item,price):
#     print(f'{qty} {item} cost ${price:2f}')
    
# f(6,'banana',1.74)
# f('banana',6,1.74)
# f(6,1.74,'banana')
# f(6,'banana',1.74)

# vi du
def tinh_trung_binh(*args):
    #kiem tra gia tri trong args
    tong = 0
    for i in args:
        tong = tong + i
    trung_binh = tong/len(args)
    return trung_binh

tinh_trung_binh(1,2,3,4,5,6,7,8,9,10)

list_ttsv =[]
def nhap_thong_tin_sv(**kwargs):
    # kiem tra cac gia tri trong kwargs
    if kwargs["diem_tb"] >=7:
        kwargs["lop"] = "A1"
    elif kwargs["diem_tb"] >=4:
        kwargs["lop"] = "A2"
    else:
        kwargs["lop"] ="A3"

nhap_thong_tin_sv(ten="trung",tuoi="18",diem_tb="5.0")


def tinh_tong_hai_so(a:int = 1,b:int = 2) -> float:
    """
    ham tinh toan nhan vao hai so a va b
    tra ve tong hai so nay
    
    """
    
    
    return a + b
tinh_tong_hai_so(4,5)


print("abc","sjj ",1)

sum()




