one_BTC = 1168 # lv
one_yuan = 0.15 # $
one_usd = 1.76 # lv
one_euro = 1.95 # lv

BTC = int(input())
yuan = float(input())
comm = float(input())

ttl_BTC = one_BTC * BTC # lv
ttl_yuan = one_yuan * yuan # $
ttl_leva = ttl_yuan * one_usd + ttl_BTC
ttl_euro = ttl_leva / one_euro * (100 - comm) / 100
print(f'{ttl_euro:.2f}')