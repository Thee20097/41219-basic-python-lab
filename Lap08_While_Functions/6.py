def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

while True:
  print("1. บวกเลขสองจำนวน")
  print("2. ลบเลขสองจำนวน")
  print("3. คูณเลขสองจำนวน")
  print("4. ออก")
  choice = int(input())
  
  if choice == 4:
    print("จบโปรแกรม")
    break

  a = int(input())
  b = int(input())

  if choice == 1:
    print("ผลลัพธ์:",add(a,b))
  elif choice == 2:
    print("ผลลัพธ์:",sub(a,b))
  elif choice == 3:
    print("ผลลัพธ์:",mul(a,b))
