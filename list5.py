#List-5
#Dylan and Avi
#12/13/17

def main():
    print "You will be asked for a string and the amount of vowels in the string will be displayed."
    string = raw_input("Enter a string: ")
    count = 0
    vowels = ['a','e','i','o','u','y']
    for i in string:
        if i in vowels:
            count += 1
    print "The amount of vowels in the string are", count

main()
