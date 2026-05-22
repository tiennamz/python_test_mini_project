'''
Câu 1: Khởi động - Tính tiền thanh toán (3 điểm) 
Viết chương trình tính tiền mua hàng cho khách.
Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
Tính Tổng tiền = Đơn giá * Số lượng.
Áp dụng logic khuyến mãi:
Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
Nếu Tổng tiền < 1.000.000, không giảm giá.
In ra màn hình số tiền cuối cùng khách phải thanh toán.


'''
price = int(input("Vui lòng nhập vào giá bá sản phẩm: "))
quantity = int(input("Bạn muốn mua tổng bao nhiêu hàng hóa: "))

total_money = price * quantity

if total_money > 1000000:
    total_money = total_money * 0.9
print(f"Bạn cần phải trả: {total_money} VND")













