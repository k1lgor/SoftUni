deg = int(input())
daytime = str(input())
if daytime == 'Morning':
    if 10 <= deg <= 18:
        print(f"It's {deg} degrees, get your Sweatshirt and Sneakers.")
    elif 18 < deg <= 24:
        print(f"It's {deg} degrees, get your Shirt and Moccasins.")
    elif deg >= 25:
        print(f"It's {deg} degrees, get your T-Shirt and Sandals.")
elif daytime == 'Afternoon':
    if 10 <= deg <= 18:
        print(f"It's {deg} degrees, get your Shirt and Moccasins.")
    elif 18 < deg <= 24:
        print(f"It's {deg} degrees, get your T-Shirt and Sandals.")
    elif deg >= 25:
        print(f"It's {deg} degrees, get your Swim Suit and Barefoot.")
elif daytime == 'Evening':
    if 10 <= deg <= 18:
        print(f"It's {deg} degrees, get your Shirt and Moccasins.")
    elif 18 < deg <= 24:
        print(f"It's {deg} degrees, get your Shirt and Moccasins.")
    elif deg >= 25:
        print(f"It's {deg} degrees, get your Shirt and Moccasins.")
