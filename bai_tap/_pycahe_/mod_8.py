so = int(input("Nhập một số nguyên: "))
def uoc_so(n):
    uoc_list = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            uoc_list.append(i)
    return uoc_list

print(f"Các ước của {so} là: {uoc_so(so)}")
