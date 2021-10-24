guests = int(input())
one_guest = float(input())
budget = float(input())

cake = budget * 0.1

if 10 <= guests <= 15:
    one_guest *= 0.85
elif 15 < guests <= 20:
    one_guest *= 0.8
elif guests >= 20:
    one_guest *= 0.75
ttl = one_guest * guests + cake

if ttl > budget:
    print(f'No party! {abs(budget - ttl):.2f} leva needed.')
else:
    print(f'It is party time! {abs(budget - ttl):.2f} leva left.')