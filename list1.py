#List-1
#Dylan and Avi
#12/8/17

def main():
    nums = []
    tot = 0
    for i in range (10):
        digit = 0
        while digit == 0:
            num = raw_input ("Enter a number to add it to the list: ")
            if num.isdigit():
                num = int(num)
                nums.append(num)
                digit = 1
            else:
                print "Please type a valid number"
    for i in nums:
        tot = tot + i
    ave = tot/10.0
    print "Average of List: ", ave

main()
