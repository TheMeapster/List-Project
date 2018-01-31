#List-4
#Dylan and Avi
#12/8/17

from random import randint

def main():
    print "This will make a list of 101 random numbers from 1-1000 and it will find the median of the list."
    nums = []
    for i in range(101):
        num = randint(1, 1000)
        nums.append(num)
    print "The median of the list is:", nums[51]

main()
