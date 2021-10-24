packet_pens = 5.8
packet_markers = 7.2
detergent = 1.2 # per liter

pens = int(input())
markers = int(input())
liters = float(input())
discount = int(input())

discount = (100 - discount) / 100

ttl_pens = pens * packet_pens
ttl_markers = markers * packet_markers
ttl_detergent = detergent * liters
print(f'{((ttl_pens + ttl_markers + ttl_detergent) * discount):.3f}')