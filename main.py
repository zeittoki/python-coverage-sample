def main():
    price = int(input())

    if price >= 3000:
        discounted = price - 800
    elif price >= 2000:
        discounted = price - 500
    elif price >= 1500:
        discounted = price - 300
    else:
        discounted = price

    print(discounted)
