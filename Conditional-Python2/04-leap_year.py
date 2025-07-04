# รับปี ค.ศ. จากผู้ใช้
year = int(input("Enter a year: "))
# ตรวจสอบเงื่อนไขปีอธิกสุรทิน
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")  # เป็นปีอธิกสุรทิน
else:
    print("Not a Leap Year") # ไม่เป็นปีอธิกสุรทิน