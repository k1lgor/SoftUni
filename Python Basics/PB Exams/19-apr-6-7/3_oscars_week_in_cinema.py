film_name = input()
room = input()
tickets = int(input())
tick = 0
ticket = 0
if film_name == 'A Star Is Born':
    if room == 'normal':
        tick = 7.5
    elif room == 'luxury':
        tick = 10.5
    elif room == 'ultra luxury':
        tick = 13.5
elif film_name == 'Bohemian Rhapsody':
    if room == 'normal':
        tick = 7.35
    elif room == 'luxury':
        tick = 9.45
    elif room == 'ultra luxury':
        tick = 12.75
elif film_name == 'Green Book':
    if room == 'normal':
        tick = 8.15
    elif room == 'luxury':
        tick = 10.25
    elif room == 'ultra luxury':
        tick = 13.25
elif film_name == 'The Favourite':
    if room == 'normal':
        tick = 8.75
    elif room == 'luxury':
        tick = 11.55
    elif room == 'ultra luxury':
        tick = 13.95

ticket = tick * tickets
print(f'{film_name} -> {ticket:.2f} lv.')