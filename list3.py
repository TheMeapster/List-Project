#List-3
#Dylan and Avi
#12/8/17

from random import randint

def main():
    count = 0
    nums = []
    for i in range(50):
        num = randint(1, 50)
        nums.append(num)
    for i in nums:
        if i == 27:
            count = count + 1
    nums.sort()
    print "The number 27 is in the list", count, "times."
    print "The list is:", nums

main()
