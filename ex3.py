print("===== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ =====")

for employee_number in range(1, 4):

    print("\n--- Nhập thông tin nhân viên", employee_number, "---")

    employee_id = input("Nhập mã nhân viên: ").strip()
    full_name = input("Nhập họ và tên: ").strip()
    department = input("Nhập phòng ban: ").strip()

    if employee_id == "" or full_name == "":
        print("[CẢNH BÁO] Dữ liệu hoặc mã không hợp lệ ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        continue

    print("\n===== HỒ SƠ NHÂN SỰ =====")
    print("Mã nhân viên:", employee_id)
    print("Họ và tên:", full_name)
    print("Phòng ban:", department)
    print("=========================")

print("\nĐã hoàn tất onboarding cho 3 nhân viên!")