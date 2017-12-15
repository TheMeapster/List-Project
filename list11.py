#List-11
#Dylan and Avi
#12/15/17

def main():
    string1 = raw_input("Enter a string:")
    string2 = raw_input("Enter another string: ")
    list1 = []
    for i in string1:
        if i.isalpha:
            letters.append(i)
        else:
            
    count = 0
    for i in string1:
        if i in string2:
            count += 1
            if count == len(string1):
                print string1, "and", string2, "are anograms."
        else:
            print string1, "and", string2, "are not anograms."
main()
