# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests, sys

if len(sys.argv) != 2:
   sys.exit('Missing command-line argument')
else:
    try:
        s = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = response.json()['bpi']['USD']['rate_float']
    amount = price * s
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit()
