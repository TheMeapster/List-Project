#List-1
#DM and AS
#12/8/17

def main():
    print "You will be asked to input 10 numbers and the average of those numbers will be calculated and displayed."
    nums = []
    tot = 0
    for i in range(10):
        digit = 0
        while digit == 0:
            num = raw_input("Enter a number to add it to the list: ")
            if num.isdigit():
                num = int(num)
                nums.append(num)
                digit = 1
            else:
                print "That is not a number."
    for i in nums:
        tot = tot + i
    ave = tot/10.0
    print "The average is:", ave

main()
