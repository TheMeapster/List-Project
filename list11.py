#List-11
#Dylan and Avi
#12/15/17
def validInput():
    valid = 1
    while valid == 1:
        string = raw_input("Enter a string of just letters: ")
        valid2 = 1
        while valid2 == 1:
            for i in string:
                print i
                if i.isalpha:
                    if i == string[-1]:
                        return string
                else:
                    print "That is not a valid string."
                    valid2 = 0
                    continue

def main():
    string1 = validInput()
    string2 = validInput()
    list1 = []
    list2 = []
    for i in string1:
        list1.append(i)
    for i in string2:
        list2.append(i)
    count = 0
    for i in list1:
        if i in list2:
            list2.remove(i)
            count += 1
            if count == len(string1):
                print string1, "and", string2, "are anograms."
        else:
            print string1, "and", string2, "are not anograms."
            return
main()
