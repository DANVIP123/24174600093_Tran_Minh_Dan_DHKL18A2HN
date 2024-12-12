so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))
def ucln(a, b):
    if b == 0:
        return abs(a)
    return ucln(b, a % b)
print(f"UCLN của {so1} và {so2} là: {ucln(so1, so2)}")
