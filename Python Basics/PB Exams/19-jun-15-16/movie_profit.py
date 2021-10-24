name = input()
days = int(input())
tickets = int(input())
price = float(input())
percent_for_cinema = int(input())

ttl = days * tickets * price
cinema = ttl * percent_for_cinema / 100
ttl -= cinema
print(f'The profit from the movie {name} is {ttl:.2f} lv.')