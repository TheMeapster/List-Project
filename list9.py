print 'This is an ASCII encryptor or decryptor'

def decrypt(x):
    ASCII = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
    convertFlip = dict((v,k) for k,v in x.iteritems())
    convertFinal={}
    for i in sorted(convertFlip.iterkeys()):
        convertFinal[i]=convertFlip[i]
    goodInput = 0
    while goodInput == 0:
        goodInput = 1
        message = raw_input('Enter the encoded message with each number seperated by a space: ')
        message = message.split(' ')
        for i in message:
            mesdig = 0
            while mesdig == 0:
                if i.isdigit():
                    if int(i) <= 126:
                        mesdig = 1
                        i = int(i)
                    else:
                        print "That is not a valid message."
                        mesdig = 1
                        goodInput = 0
                else:
                    print "That is not a valid message."
                    mesdig = 1
                    goodInput = 0
    digit = 0
    while digit == 0:
        key = raw_input('Enter a key: ')
        if key.isdigit():
            key = int(key)
            digit = 1
        else:
            print "That is not a valid key."
    final = ''
    for i in message:
        i = int(i)
        while abs(key) > len(ASCII):
            if key < 0:
                key = key + len(ASCII)
            elif key > 0:
                key = key - len(ASCII)
        else:
            if ASCII.index(i) + key + 1 > len(ASCII):
                place = ASCII.index(i) - len(ASCII) - key
                i = ASCII[place]
                final += str(convertFlip[i])
            else:
                i = ASCII[ASCII.index(i) - key]
                final += str(convertFlip[i])
    print final

def encrypt(x):
    ASCII = [' ', '!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?', '@', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
    message = raw_input('Enter a message: ')
    digit = 0
    while digit == 0:
        key = raw_input('Enter a key: ')
        if key.isdigit():
            digit = 1
            key = int(key)
        else:
            print "That is not a valid key."
    characters = []
    final = ''
    for i in message:
        characters.append(i)
    for i in characters:
        while abs(key) > len(ASCII):
            if key < 0:
                key = key + len(ASCII)
            elif key > 0:
                key = key - len(ASCII)
        else:
            if ASCII.index(i) + key + 1 > len(ASCII):
                place = ASCII.index(i) - len(ASCII) + key
                i = ASCII[place]
                final += str(x[i]) + ' '
            else:
                i = ASCII[ASCII.index(i)+key]
                final += str(x[i]) + ' '
    print final

def main():
    convert = {' ': 32, '!': 33, '\"': 34, '#': 35, '$': 36, '%': 37, '&': 38, '\'': 39, '(': 40, ')': 41, '*': 42, '+':43, ',': 44, '-': 45, '.': 46, '/': 47,'0': 48,'1': 49,'2': 50, '3': 51,'4': 52,'5':53,'6':54,'7':55,'8':56,'9':57,':':58,';':59,'<':60,'=':61,'>':62,'?':63,'@':64,'A':65,'B':66,'C':67,'D':68,'E':69,'F':70, 'G':71,'H':72,'I':73,'J':74,'K':75,'L':76,'M':77,'N':78,'O':79,'P':80,'Q':81,'R':82,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88,'Y':89,'Z':90,'[':91,'\\':92,']':93,'^':94,'_':95,'`':96,'a':97,'b':98,'c':99,'d':100,'e':101,'f':102,'g':103,'h':104,'i':105,'j':106,'k':107,'l':108,'m':109,'n':110,'o':111,'p':112,'q':113,'r':114,'s':115,'t':116,'u':117,'v':118,'w':119,'x':120,'y':121,'z':122,'{':123,'|':124,'}':125,'~':126}
    choice = raw_input("Would you like to encrypt(e) or decrypt(d) a message: ")
    if choice == 'e':
        encrypt(convert)
    elif choice == 'd':
        decrypt(convert)
    else:
        print 'That is not a valid choice'
        main()

main()
