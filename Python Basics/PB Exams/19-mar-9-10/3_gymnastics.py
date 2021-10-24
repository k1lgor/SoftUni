country = input()
tool = input()
diff = 0
exe = 0
ttl = 0
if tool == 'ribbon':
    if country == 'Russia':
        diff = 9.100
        exe = 9.400
    elif country == 'Bulgaria':
        diff = 9.600
        exe = 9.400
    elif country == 'Italy':
        diff = 9.200
        exe = 9.500
elif tool == 'hoop':
    if country == 'Russia':
        diff = 9.300
        exe = 9.800
    elif country == 'Bulgaria':
        diff = 9.550
        exe = 9.750
    elif country == 'Italy':
        diff = 9.450
        exe = 9.350
elif tool == 'rope':
    if country == 'Russia':
        diff = 9.600
        exe = 9.000
    elif country == 'Bulgaria':
        diff = 9.500
        exe = 9.400
    elif country == 'Italy':
        diff = 9.700
        exe = 9.150

ttl = diff + exe
print(f'The team of {country} get {ttl:.3f} on {tool}.')
print(f'{((20 - ttl) / 20 * 100):.2f}%')