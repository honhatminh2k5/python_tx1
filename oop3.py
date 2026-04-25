class NhanVien:
    def __init__(self, ma_so, ho_ten,luong_co_ban):
        self.ma_so= ma_so
        self.ho_ten= ho_ten
        self.luong_co_ban= luong_co_ban

    def tinh_luong(self):
        return self.luong_co_ban
    
class NhanVienBanHang(NhanVien):
    def __init__(self, ma_so, ho_ten, luong_co_ban, doanh_so):
        super().__init__(ma_so, ho_ten, luong_co_ban)
        self.doanh_so= doanh_so

    def tinh_luong(self):
        return self.luong_co_ban + 0.05*self.doanh_so
    
class NhanVienQuanLy(NhanVien):
    def __init__(self, ma_so, ho_ten, luong_co_ban, so_ngay_cong):
        super().__init__(ma_so, ho_ten, luong_co_ban)
        self.so_ngay_cong= so_ngay_cong

    def tinh_luong(self):
        return self.luong_co_ban + 50*self.so_ngay_cong
    
nv_bh=NhanVienBanHang("001","Phung Thanh Do",36,63)
nv_ql=NhanVienQuanLy("036","Tu Sena",63,36)
print("----THONG TIN NHAN VIEN----")
print(f"Ma so:{nv_bh.ma_so} | Ho va ten:{nv_bh.ho_ten} | luong:{nv_bh.tinh_luong()} | doanh so:{nv_bh.doanh_so}")
print(f"Ma so:{nv_ql.ma_so} | Ho va ten:{nv_ql.ho_ten} | luong:{nv_ql.tinh_luong()} | doanh so:{nv_ql.so_ngay_cong}")