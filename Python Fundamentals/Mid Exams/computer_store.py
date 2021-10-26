def customer(current_total, current_total_wout_tax):

    if current_total == 0:
        return print("Invalid order!")
    if order == 'special':
        current_total *= 0.9
    return print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {current_total_wout_tax:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {current_total:.2f}$")


total_wout_tax = 0
total = 0
taxes = 0

while True:

    order = input()

    if order in ['special', 'regular']:
        break

    price = float(order)
    if price < 0:
        print("Invalid price!")
        continue

    total_wout_tax += price
    taxes += price * 0.2
    total = total_wout_tax + taxes

customer(total, taxes, total_wout_tax)
