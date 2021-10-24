from math import floor
rec_in_sec = float(input())
dist_in_m = float(input())
one_m_in_sec = float(input())

ttl_time = dist_in_m * one_m_in_sec
delay = floor(dist_in_m / 50) * 30 # sec
ttl_time += delay

if ttl_time >= rec_in_sec:
    print(f'No! He was {abs(ttl_time - rec_in_sec):.2f} seconds slower.')
else:
    print(f'Yes! The new record is {ttl_time:.2f} seconds.')