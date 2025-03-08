class SinhVien:
    # Biến class để tự động tăng mã sinh viên
    id_counter = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        self.id = SinhVien.id_counter
        SinhVien.id_counter += 1
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_trung_binh = diem_trung_binh
        self.hoc_luc = self.tinh_hoc_luc()

    def tinh_hoc_luc(self):
        if self.diem_trung_binh >= 8:
            return "Giỏi"
        elif self.diem_trung_binh >= 6.5:
            return "Khá"
        elif self.diem_trung_binh >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"ID: {self.id}, Tên: {self.ten}, Giới tính: {self.gioi_tinh}, Chuyên ngành: {self.chuyen_nganh}, Điểm trung bình: {self.diem_trung_binh}, Học lực: {self.hoc_luc}"

class QuanLySinhVien:
    def __init__(self):
        self.sinh_vien_list = []

    def them_sinh_vien(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        sinh_vien = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        self.sinh_vien_list.append(sinh_vien)
        print(f"Đã thêm sinh viên: {sinh_vien}")

    def cap_nhat_sinh_vien(self, id, ten=None, gioi_tinh=None, chuyen_nganh=None, diem_trung_binh=None):
        for sv in self.sinh_vien_list:
            if sv.id == id:
                if ten:
                    sv.ten = ten
                if gioi_tinh:
                    sv.gioi_tinh = gioi_tinh
                if chuyen_nganh:
                    sv.chuyen_nganh = chuyen_nganh
                if diem_trung_binh is not None:
                    sv.diem_trung_binh = diem_trung_binh
                    sv.hoc_luc = sv.tinh_hoc_luc()  # Cập nhật lại học lực
                print(f"Đã cập nhật thông tin sinh viên: {sv}")
                return
        print("Không tìm thấy sinh viên với ID đó!")

    def xoa_sinh_vien(self, id):
        for sv in self.sinh_vien_list:
            if sv.id == id:
                self.sinh_vien_list.remove(sv)
                print(f"Đã xóa sinh viên: {sv}")
                return
        print("Không tìm thấy sinh viên với ID đó!")

    def hien_thi_sinh_vien(self):
        if not self.sinh_vien_list:
            print("Danh sách sinh viên rỗng.")
        else:
            for sv in self.sinh_vien_list:
                print(sv)

def menu():
    quan_ly = QuanLySinhVien()
    
    while True:
        print("\nChương trình quản lý sinh viên")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Thoát")
        
        chon = input("Chọn chức năng (1-5): ")
        
        if chon == "1":
            ten = input("Nhập tên sinh viên: ")
            gioi_tinh = input("Nhập giới tính sinh viên: ")
            chuyen_nganh = input("Nhập chuyên ngành sinh viên: ")
            diem_trung_binh = float(input("Nhập điểm trung bình sinh viên: "))
            quan_ly.them_sinh_vien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        
        elif chon == "2":
            id = int(input("Nhập ID sinh viên cần cập nhật: "))
            ten = input("Nhập tên mới (hoặc bỏ qua nếu không thay đổi): ")
            gioi_tinh = input("Nhập giới tính mới (hoặc bỏ qua nếu không thay đổi): ")
            chuyen_nganh = input("Nhập chuyên ngành mới (hoặc bỏ qua nếu không thay đổi): ")
            diem_trung_binh = input("Nhập điểm trung bình mới (hoặc bỏ qua nếu không thay đổi): ")
            diem_trung_binh = float(diem_trung_binh) if diem_trung_binh else None
            quan_ly.cap_nhat_sinh_vien(id, ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        
        elif chon == "3":
            id = int(input("Nhập ID sinh viên cần xóa: "))
            quan_ly.xoa_sinh_vien(id)
        
        elif chon == "4":
            quan_ly.hien_thi_sinh_vien()
        
        elif chon == "5":
            print("Thoát chương trình.")
            break
        
        else:
            print("Chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    menu()
