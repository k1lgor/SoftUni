import math
record_in_sec = float(input())
dist_in_m = float(input())
sec_for_1m = float(input())

dist_in_sec = dist_in_m * sec_for_1m

delay = math.floor(dist_in_m / 15) * 12.5

ttl_time = dist_in_sec + delay

if ttl_time < record_in_sec:
    print(
        f'Yes, he succeeded! The new world record is {ttl_time:.2f} seconds.')
else:
    print(
        f'No, he failed! He was {abs(record_in_sec - ttl_time):.2f} seconds slower.')
