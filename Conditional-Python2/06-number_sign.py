# รับค่าจำนวนเต็มจากผู้ใช้
number = int(input("Enter an integer: "))
if number > 0:
    print("Positive") # ตัวเลขเป็นบวก
elif number < 0:
    print("Negative") # ตัวเลขเป็นลบ
else:
    print("Zero") # ตัวเลขเป็นศูนย์