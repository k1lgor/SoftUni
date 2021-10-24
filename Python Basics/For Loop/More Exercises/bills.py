month = int(input())
elec = 0.0
water = 0.0
net = 0.0
other = 0.0
for _ in range(1, month + 1):
    electax = float(input())
    elec += electax
water = month * 20
net = month * 15
other = (elec + water + net) * 1.2
ttl = elec + water + net + other
print(f'Electricity: {elec:.2f} lv\nWater: {water:.2f} lv\nInternet: {net:.2f} lv\nOther: {other:.2f} lv\nAverage: {(ttl / month):.2f} lv')
