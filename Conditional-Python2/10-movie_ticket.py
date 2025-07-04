# คำนวณราคาตั๋วตามอายุและวันในสัปดาห์
age = int(input("Enter age: "))
day = int(input("Enter day of week (1-7): "))
# ราคาตั๋วพื้นฐาน
if age < 13:
    price = 100
elif age <= 60: 
    price = 180
else: # อายุ > 60
    price = 120
# ค่าบริการเพิ่มเติมในช่วงวันหยุด
if day == 6 or day == 7: # วันเสาร์ กับ อาทิตย์
    price += 50
print(f"Total ticket price: {price} baht")