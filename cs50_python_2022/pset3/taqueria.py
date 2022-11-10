# https://cs50.harvard.edu/python/2022/psets/3/taqueria/

def main():
    prices = {"baja taco": 4.00,
              "burrito": 7.50,
              "bowl": 8.50,
              "nachos": 11.00,
              "quesadilla": 8.50,
              "super burrito": 8.50,
              "super quesadilla": 9.50,
              "taco": 3.00,
              "tortilla salad": 8.00}
    print(prices)
    cost = 0
    while True:
        try:
            item = input('Item: ')
            if item.lower() in prices:
                cost += prices[item.lower()]
            print('$', end='')
            print('{:.2f}'.format(cost))
        except EOFError:
            print()
            break

main()
