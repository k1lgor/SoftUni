num = float(input())

if 35 >= num >= 26:
    print('Hot')
elif 25.99 >= num >= 20.1:
    print('Warm')
elif 20 >= num >= 15:
    print('Mild')
elif 14.9 >= num >= 12:
    print('Cool')
elif 11.9 >= num >= 5:
    print('Cold')
else:
    print('unknown')
