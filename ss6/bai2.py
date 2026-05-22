# Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật (4 điểm) 
# Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình.

correct_password = "123456"
is_correct = False
for i in range(1,5):
    input_password = input("Vui lòng nhập mật khẩu: ")
    if input_password == correct_password:
        is_correct = True
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
    
if is_correct == False:
    print("Tài khoản đã bị khóa!")










