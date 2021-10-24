name = input()
tickets_old = int(input())
tickets_kid = int(input())
net_old = float(input())
other = float(input())

kid = net_old * 0.3
ttl_old = net_old + other
ttl_kid = kid + other
ttl = tickets_kid * ttl_kid + tickets_old * ttl_old
profit = ttl * 0.2
print(f'The profit of your agency from {name} tickets is {profit:.2f} lv.')