season = input()
group = input()
ppl = int(input())
nights = int(input())
sport = ''
sum = 0.0
if season == 'Winter':
    if group == 'girls' or group == 'boys':
        sum = ppl * 9.6 * nights
        if ppl >= 50:
            sum *= 0.5
        elif 20 <= ppl < 50:
            sum *= 0.85
        elif 10 <= ppl < 20:
            sum *= 0.95
        if group == 'girls':
            sport = 'Gymnastics'
        else:
            sport = 'Judo'
    else:
        sport = 'Ski'
        sum = ppl * 10 * nights
        if ppl >= 50:
            sum *= 0.5
        elif 20 <= ppl < 50:
            sum *= 0.85
        elif 10 <= ppl < 20:
            sum *= 0.95
elif season == 'Spring':
    if group == 'girls' or group == 'boys':
        sum = ppl * 7.2 * nights
        if ppl >= 50:
            sum *= 0.5
        elif 20 <= ppl < 50:
            sum *= 0.85
        elif 10 <= ppl < 20:
            sum *= 0.95
        if group == 'girls':
            sport = 'Athletics'
        else:
            sport = 'Tennis'
    else:
        sport = 'Cycling'
        sum = ppl * 9.5 * nights
        if ppl >= 50:
            sum *= 0.5
        elif 20 <= ppl < 50:
            sum *= 0.85
        elif 10 <= ppl < 20:
            sum *= 0.95
elif season == 'Summer':
    if group == 'girls' or group == 'boys':
        sum = ppl * 15 * nights
        if ppl >= 50:
            sum *= 0.5
        elif 20 <= ppl < 50:
            sum *= 0.85
        elif 10 <= ppl < 20:
            sum *= 0.95
        if group == 'girls':
            sport = 'Volleyball'
        else:
            sport = 'Football'
    else:
        sport = 'Swimming'
        sum = ppl * 20 * nights
        if ppl >= 50:
            sum *= 0.5
        elif 20 <= ppl < 50:
            sum *= 0.85
        elif 10 <= ppl < 20:
            sum *= 0.95
print(f'{sport} {sum:.2f} lv.')
