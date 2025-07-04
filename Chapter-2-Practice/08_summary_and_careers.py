bill, tip, people = map(float, input().split())
total = bill + (bill * tip / 100)
each = total / people
print("Each person pays:", round(each, 2))
