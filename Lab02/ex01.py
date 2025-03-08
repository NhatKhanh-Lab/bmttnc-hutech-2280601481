def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

num_List = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, num_List.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong day so la: ", tong_chan)