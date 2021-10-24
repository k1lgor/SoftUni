time = input()
type_contract = input()
mobile = input()
months = int(input())
tax = 0
ttl = 0

if time == 'one':
    if type_contract == 'Small':
        tax = 9.98
    elif type_contract == 'Middle':
        tax = 18.99
    elif type_contract == 'Large':
        tax = 25.98
    elif type_contract == 'ExtraLarge':
        tax = 35.99
elif time == 'two':
    if type_contract == 'Small':
        tax = 8.58
    elif type_contract == 'Middle':
        tax = 17.09
    elif type_contract == 'Large':
        tax = 23.59
    elif type_contract == 'ExtraLarge':
        tax = 31.79

if mobile == 'yes':
    if tax <= 10:
        tax += 5.5
    elif 10 < tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85
ttl = tax * months
if time == 'two':
    ttl *= 0.9625
print(f'{ttl:.2f} lv.')