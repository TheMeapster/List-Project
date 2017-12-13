#List-6
#Dylan and Avi
#12/13/17

def main():
    print "You will be asked for a string and the number of non-space characters will be displayed."
    string = raw_input("Enter a string: ")
    count = len(string)
    countSpace = 0
    for i in string:
        if i == " ":
            countSpace += 1
    countNon = count - countSpace
    print "The numer of non-space characters is:", countNon

main()
