last_sector = input()
rows_fsector = int(input())
seats_odd = int(input())
counter = 0
for sector in range(65, ord(last_sector) + 1):
    for row in range(1, rows_fsector + 1):
        if row % 2 != 0:
            for seats in range(ord('a'), ord('a') + seats_odd):
                print(f'{chr(sector)}{row}{chr(seats)}')
                counter += 1
        else:
            for seats in range(ord('a'), ord('a') + seats_odd + 2):
                print(f'{chr(sector)}{row}{chr(seats)}')
                counter += 1
    if rows_fsector + 1 > rows_fsector:
        rows_fsector += 1
print(counter)
