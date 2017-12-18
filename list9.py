def main():
    ASCII = [' ', '!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/']
    convert = {' ': '32', '!': '33', '\"': '34', '#': '35', '$': '36', '%': '37', '&': '38', '\'': '39', '(': '40', ')': '41', '*': '42', '+':'43', ',': '44', '-': '45', '.': '46', '/': '47'}
    message = raw_input('Enter a message: ')
    digit = 0
    while digit == 0:
        key = raw_input('Enter a key: ')
        if key.isdigit():
            key = int(key)
            digit = 1
        else:
            print 'That is not a valid key.'
    characters = []
    final = ''
    for i in message:
        characters.append(i)
    for i in characters:
        i = ASCII[ASCII.index(i)+key]
        final += convert[i] + ', '
    print final

main()
