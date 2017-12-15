#List-11
#Dylan and Avi
#12/15/17
def validInput():
    valid = 1
    while valid == 1:
        string1 = raw_input("Enter a string of just letters: ")
        string2 = raw_input("Enter another string letters: ")
        for i in string1:
            if i.isalpha:
                list1.append(i)
            else:
                print "That is not a valid string."
                return
def main():
    list1 = validInput()
    count = 0
    for i in string1:
        if i in string2:
            count += 1
            if count == len(string1):
                print string1, "and", string2, "are anograms."
        else:
            print string1, "and", string2, "are not anograms."
main()
