# รับค่าปีจากผู้ใช้
day = int(input("Enter day number (1-7): "))
# ตรวจสอบเงื่อนไขปีอธิกสุรทิน
if 1 <= day <= 5:  
    print("Weekday") # เป็นปีอธิกสุรทิน
elif 6 <= day <= 7: 
    print("Weekend") # ไม่เป็นปีอธิกสุรทิน
else:
    print("Invalid day number. Please enter 1-7.")  