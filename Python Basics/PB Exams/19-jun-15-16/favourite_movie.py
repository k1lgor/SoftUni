movies = ''
best_movie = ''
cur_points = 0
best_points = 0
counter = 0

while movies != 'STOP':

    if counter == 7:
        print('The limit is reached.')
        print(f'The best movie for you is {best_movie} with {best_points} ASCII sum.')
        break
    movies = input()
    for _ in range(7):
        if movies == 'STOP':
            print(f'The best movie for you is {best_movie} with {best_points} ASCII sum.')
            break
        length = len(movies)
        for digit in movies:
            cur_points += ord(digit)
            if 97 <= ord(digit) <= 122:
                cur_points -= (2 * length)
            elif 65 <= ord(digit) <= 90:
                cur_points -= length
        if cur_points > best_points:
            best_points = cur_points
            best_movie = movies
        cur_points = 0

        counter += 1
        break