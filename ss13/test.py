id = 0
list_car = []
menu = '''
-----------------------------------------------
        QUẢN LÝ BÃI XE - SMART PARKING
-----------------------------------------------

1. Thêm xe mới vào bãi
2. Hiển thị danh sách xe trong bãi
3. Tìm kiếm xe theo mã (id)
4. Xóa xe khỏi bãi (khi xe ra)
5. Thoát chương trình'''

while True:
    print(menu)
    choice = input("Mời bạn nhận lựa chọn: ").strip()
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Mời bạn nhập số dương 1-5!")
        continue
    match choice:
        case 1:
            id +=1
            while True:
                type_of_car = input("Mời bạn nhập loại xe: ").strip()
                if not type_of_car:
                    print("Loại xe đang trống!")
                else:
                    break
                    
            while True:
                owner_of_car = input("Mời bạn nhập chủ xe: ").strip()
                if not owner_of_car:
                    print("Chủ xe đang trống!")
                else:
                    break
                
            new_car = {'id': id, 'type': type_of_car, 'owner': owner_of_car}
            
            list_car.append(new_car)
            print("Đã thêm 1 xe mới")
            
        case 2:
            if not list_car:
                print("Bãi xe hiện đang trống!")
                continue
            
            print(f"{"ID":<4}| {"Loại xe":<10}| {"Chủ xe":<15}")
            print("-" * 29)
            for car in list_car:
                print(f"{car.get("id"):<4}| {car.get("type"):<10}| {car.get("owner"):<15} ")
                print("-" * 29)

        case 3:
            if not list_car:
                print("Bãi xe hiện đang trống!")
                continue
            id_input = input("Mời bạn nhập id xe cần tìm: ").strip()
            if id_input.isdigit():
                id_input = int(id_input)
            else:
                print("Id xe phải là số dương")
                continue
            is_found = False
            for car in list_car:
                if car["id"] == id_input:
                    print(car)
                    is_found = True
                    break
            if not is_found:
                print("Xe không tồn tại")
                
        case 4:
            if not list_car:
                print("Bãi xe hiện đang trống!")
                continue
            id_input = input("Mời bạn nhập id xe cần xóa: ").strip()
            if id_input.isdigit():
                id_input = int(id_input)
            else:
                print("Id xe phải là số dương")
                continue
            is_found = False
            for index,car in enumerate(list_car):
                if car["id"] == id_input:
                    car_delete = list_car.pop(index)
                    print(f"Đã xóa xe {car_delete}")
                    is_found = True
                    break
            if not is_found:
                print("Xe không tồn tại")
                
        case 5: 
            print("Đã thoát chương trình")
            break
        case _:
            print("Mời bạn nhập lại lựa chọn")