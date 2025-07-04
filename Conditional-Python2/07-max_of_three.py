# รับค่าจำนวนเต็ม 3 จำนวน
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
# หาค่ามากที่สุด
max_value = num1  # กำหนดค่าเริ่มต้นเป็นจำนวนแรก
if num2 > max_value:
    max_value = num2
if num3 > max_value:
    max_value = num3
# แสดงผลลัพธ์
print(f"The maximum value is: {max_value}")