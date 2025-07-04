# รับคะแนนสอบจากผู้ใช้
score = int(input("Enter your score: "))
if score >= 50:
    print("Pass")  # คะแนนมากกว่าหรือเท่ากับ 50 แสดงผล "Pass"
else:
    print("Fail")   # คะแนนน้อยกว่า 50 แสดงผล "Fail"