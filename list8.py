#List-8
#Dylan and Avi
#12/14/17

def main():
    print "There is a predetermined string of numbers. The string will be sorted from least to greatest and it will be sorted alphabetically (eight, five, four, etc.)."
    string = '8295815097991628184014892095210417542494818618938024213152859970499140884256647420351285241154616293'
    nums = []
    stringSort = ''
    stringAlpha = ''
    for i in string:
        nums.append(i)
    nums.sort()
    for i in nums:
        stringSort += i
    print "The string sorted from least to greatest is:", stringSort
    keys = ['8', '5', '4', '9', '1', '7', '6', '3', '2', '0']
    for i in keys:
        for x in string:
            if x == i:
                stringAlpha = stringAlpha + x
    print "The numbers sorted alphabetically are:", stringAlpha
main()
