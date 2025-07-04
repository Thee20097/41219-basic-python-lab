# รับยอดซื้อจากผู้ใช้
amount = float(input("Enter purchase amount: "))
if amount > 2000:
    discount = 0.15  # ส่วนลด 15% ถ้ายอดซื้อมากกว่า 2000 บาท
elif amount > 1000:
    discount = 0.10  # ส่วนลด 10% ถ้ายอดซื้อมากกว่า 1000 บาท
elif amount > 500:
    discount = 0.05  # ส่วนลด 5% ถ้ายอดซื้อมากกว่า 500 บาท
else:
    discount = 0.00  # ไม่มีส่วนลด ถ้ายอดซื้อน้อยกว่าหรือเท่ากับ 500 บาท
total = amount - (amount * discount) # คำนวณราคาสุทธิ
print(f"Total after discount: {total:.2f} baht") # แสดงผลราคาสุทธิ