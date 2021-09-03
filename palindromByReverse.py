string = input('Enter the string: ')
lower_string = ''.join(string.lower().split())
rev_str = (lower_string[::-1])
if lower_string == rev_str:
    print('String is palindrom')
else:
    print('string is not palindrom')