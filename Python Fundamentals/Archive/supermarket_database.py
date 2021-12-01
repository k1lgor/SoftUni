def product_checker(s, d):
    prod, price, qty = d.split()
    if prod not in s:
        s[prod] = {'price': float(price), 'qty': int(qty)}
    else:
        s[prod]['price'] = float(price)
        s[prod]['qty'] += int(qty)
    return s


def stoke(s):
    for k, v in s.items():
        print(
            f"{k}: ${v['price']:.2f} * {v['qty']} = ${v['price'] * v['qty']:.2f}")
    print("------------------------------")
    total = sum(v['price'] * v['qty'] for k, v in s.items())
    print(f"Grand Total: ${total:.2f}")


data = input()
store = {}

while 'stocked' not in data:

    product_checker(store, data)

    data = input()

stoke(store)
