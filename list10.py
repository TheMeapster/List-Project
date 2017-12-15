#List-7
#Dylan and Avi
#12/14/17

def main():
    print "You will be asked for a string and it will be determined if it is a palindrome."
    string = raw_input("Enter a string: ")
    letters = []
    for i in string:
        if i.isalpha() or i.isdigit():
            letters.append(i)
    print letters
    minimum = 0
    maximum = len(letters)-1
    palindrome = True
    while palindrome == True:
        if minimum <= maximum:
            if letters[minimum] == letters[maximum]:
                palindrome = True
            else:
                palindrome = False
                print string, "is not a palindrome."
                return
            minimum += 1
            maximum -= 1
        else:
            palindrome = True
            print string, "is a palindrome."
            return

main()
