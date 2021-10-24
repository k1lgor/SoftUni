str_price = float(input())
bananas_qnty = float(input())
oranges_qnty = float(input())
rasp_qnty = float(input())
str_qnty = float(input())

rasp_price = str_price / 2
oranges_price = rasp_price * 0.6
bananas_price = rasp_price * 0.2

print(
    f"{(str_price * str_qnty) + (rasp_price * rasp_qnty) + (oranges_price * oranges_qnty) + (bananas_price * bananas_qnty):.3f}"
)
