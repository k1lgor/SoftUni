products = {}
command = input()
while command != 'statistics':
    
    args = command.split(': ')
    product = args[0]
    qnty = int(args[1])
    
    if product not in products:
        products[product] = 0
    products[product] += qnty
    
    command = input()

print(f"Products in stock:")
for (product, qnty) in products.items():
    print(f"- {product}: {qnty}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
    
    
    