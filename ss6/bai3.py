# Câu 3: Nâng cao - Thống kê lô hàng nhập (3 điểm) 
# Giả sử thủ kho đang kiểm đếm một lô hàng gồm nhiều thùng. Hãy viết chương trình cho phép thủ kho nhập liên tục số lượng sản phẩm của từng thùng vào hệ thống.
# Khai báo các biến cần thiết để lưu trữ Tổng số lượng sản phẩm và Số thùng hàng hợp lệ.
# Sử dụng vòng lặp để cho phép người dùng nhập liên tục số lượng của từng thùng.
# Quy tắc xử lý:
# Nếu nhập vào số âm (< 0): In ra "Số lượng không hợp lệ, bỏ qua thùng này!" (Không cộng dồn).
# Nếu nhập vào số 0: Chương trình hiểu là đã kiểm đếm xong và kết thúc quá trình nhập (Sử dụng lệnh break).
# Nếu nhập vào số dương (> 0): Cộng dồn số lượng sản phẩm và tăng biến đếm số thùng hàng.
# Khi kết thúc vòng lặp, in ra màn hình:
# Tổng số thùng hàng hợp lệ đã đếm.
# Tổng số lượng sản phẩm thu được.

total_products = 0
valid_poducts = 0

while True:
    products = int(input("Vui lòng nhập số lượng hàng hóa: "))
    
    if products < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        continue
    elif products == 0:
        print("Kết thúc chương trình")
        break
    elif products > 0:
        total_products += products 
        valid_poducts += 1
    
print("--- Thống kê lô hàng nhập ---")
print(f"Tổng số thùng hàng hợp lệ đã đếm: {valid_poducts}")
print(f"Tổng số lượng sản phẩm thu được: {total_products}")

























































