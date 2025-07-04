length_str, width_str = input("กรอกความยาวและความกว้าง (คั่นด้วยช่องว่าง): ").split()
length = int(length_str)
width = int(width_str)
area = length * width
print(area)