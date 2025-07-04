a = int(input("ใส่คะแนนเก็บ: "))
if a < 0 or a > 30:
    print("Error")
    exit()
b = int(input("ใส่คะแนนสอบกลางภาค: "))
if b < 0 or b > 30:
    print("Error")
    exit()
c = int(input("ใส่คะแนนสอบปลายภาค: "))
if c < 0 or c > 40:
    print("Error")
    exit()      
total = a + b + c
if 80 <= total <= 100:
    print("A")
elif 75 <= total <= 79:
    print("B+")
elif 70 <= total <= 74:
    print("B")
elif 65 <= total <= 69:
    print("C+")
elif 60 <= total <= 64:
    print("C")
elif 55 <= total <= 59:
    print("D+")
elif 50 <= total <= 54:
    print("D")
else:
    print("F")
