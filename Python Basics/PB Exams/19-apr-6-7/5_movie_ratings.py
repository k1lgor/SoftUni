import sys
ttl_movies = int(input())
high_rating = -sys.maxsize
high_film = ''
low_rating = sys.maxsize
low_film = ''
counter = 0
avr = 0.0
for i in range(ttl_movies):
    film = input()
    rating = float(input())

    if rating > high_rating:
        high_rating = rating
        high_film = film
    elif rating < low_rating:
        low_rating = rating
        low_film = film
    counter += 1
    avr += rating
print(f'{high_film} is with highest rating: {high_rating:.1f}\n{low_film} is with lowest rating: {low_rating:.1f}\n\
Average rating: {(avr / counter):.1f}')