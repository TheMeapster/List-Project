#List-7
#Dylan and Avi
#12/14/17

def main():
    print "You will be asked for a string, the letters of the string in uppercased form will be displayed, and the letters in lowercase form will be displayed."
    string = raw_input("Enter a string: ")
    stringLower = ""
    letters = []
    for i in string:
        letters.append(i)
    for i in letters:
        if i.isdigit():
            letters.remove(i)
        else:
            stringLower += i
    stringUpper = stringLower.upper()
    stringLower = stringLower.lower()
    print "The letters in uppercase form are:", stringUpper
    print "The letters in lowercase form are:", stringLower

main()
