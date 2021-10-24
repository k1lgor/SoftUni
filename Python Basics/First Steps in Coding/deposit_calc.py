deposit = float(input())
time = int(input())
rate = float(input())

interest_month = deposit * rate / 100 / 12
print(deposit + (time * interest_month))
