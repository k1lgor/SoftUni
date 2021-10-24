rent = int(input())

statues = rent * 0.7
catering = statues * 0.85
sound = catering / 2
print(f'{(rent + statues + catering + sound):.2f}')