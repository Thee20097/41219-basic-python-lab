eggs = int(input("กรอกจำนวนไข่ไก่ทั้งหมด: "))
trays = eggs // 30       # divide number
remaining = eggs % 30    # remainder from division

print(f"Trays: {trays} Remaining: {remaining}")