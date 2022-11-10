s = input(' ')

if 'hello' in s.lower():
    print('$0')
elif s.strip().lower()[0] == 'h':
    print('$20')
else:
    print('$100')
