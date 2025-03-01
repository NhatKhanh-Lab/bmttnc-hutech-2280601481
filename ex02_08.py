def kiem_tra_nhi_phan_chia_het_cho_5(binary_str):
    so_thap_phan = int(binary_str, 2)
    return so_thap_phan % 5 == 0


chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")


danh_sach_nhi_phan = chuoi_nhi_phan.split()


for binary_str in danh_sach_nhi_phan:
    if kiem_tra_nhi_phan_chia_het_cho_5(binary_str):
        print(f"Số nhị phân {binary_str} chia hết cho 5.")
