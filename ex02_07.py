def kiem_tra_nhi_phan_chia_het_cho_5(binary_str):
    so_thap_phan = int(binary_str, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

so_nhi_phan = input("Nhập số nhị phân: ")
if kiem_tra_nhi_phan_chia_het_cho_5(so_nhi_phan):
    print(f"Số nhị phân {so_nhi_phan} chia hết cho 5.")
else:
    print(f"Số nhị phân {so_nhi_phan} không chia hết cho 5.")
