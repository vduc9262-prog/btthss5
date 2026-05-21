

staff_quantity = int(input('nhập số lượng nhân viên: '))

for i in range(staff_quantity):
    full_name = input('nhập tên nhân viên:  ')


    day = int(input('nhập số ngày làm việc: '))
    if day < 0 or day > 22: 
        print('dữ liệu ko hợp lệ !')
        continue 
    if day == 0:
        print(f' {full_name} nghỉ cả tháng ko đi làm ngày nào !')
    else:
                
                print(f"{full_name}:", end= " ")   
                for row in range(1):
                    for colum in range(day):
                        print("*", end=" ")
                    print()
    if day >= 18: 
        print('làm việc chăm chỉ ')
    elif day < 10:
        print('làm việc ít ')
    else:
        print('làm việc bth ')
    print()
