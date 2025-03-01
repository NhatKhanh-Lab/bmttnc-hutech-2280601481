def kiem_tra_so_nguyen_to(so):
    if so <= 1:
        return False
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            return False
    return True

so_ngau_nhien = int(input("Nhập 1 số ngẫu nhiên: "))
if kiem_tra_so_nguyen_to(so_ngau_nhien):
    print(so_ngau_nhien, "là số nguyên tố")
else:
    print(so_ngau_nhien, "không là số nguyên tố")