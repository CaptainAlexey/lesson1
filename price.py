def format_price(price):
    price=int(price)
    str_line = f"Price: {price} rub."
    return str_line

print(format_price(56.24))