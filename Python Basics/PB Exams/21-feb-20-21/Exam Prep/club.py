wanted = float(input())
ttl = 0
text = ''
suma = 0
while text != 'Party!':
    if suma >= wanted:
        print('Target acquired.')
        break
    text = input()
    if text == 'Party!':
        print(f'We need {abs(wanted - suma):.2f} leva more.')
        break
    cocktails = int(input())
    name_len = len(text)
    ttl = name_len * cocktails
    if ttl % 2 != 0:
        ttl *= 0.75
    suma += ttl
print(f'Club income - {suma:.2f} leva.')