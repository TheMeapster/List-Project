#List-3
#Dylan and Avi
#12/8/17

from random import *

def main():
print "This is will make a random list of number between 1 and 50 and it will see if 27 is in the list and it will then tell you the frequency of 27."
    count = 0
    nums = []
    for i in range (50):
        num = randint (1, 50)
        nums.append(num)
    for i in nums:
        if i == 27:
            count = count + 1
        nums.sort()
            print "27 is in the list and it repeats",count,"times"
            print "The list is", nums

main()
