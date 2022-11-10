def main():
    s = input(' ')
    s = s.strip().lower().split('.')[-1]
    if s == 'gif':
        print('image/gif')
    elif s == 'jpg' or s == 'jpeg':
        print('image/jpeg')
    elif s == 'png':
        print('image/png')
    elif s == 'pdf':
        print('application/pdf')
    elif s == 'txt':
        print('text/plain')
    elif s == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')

main()
