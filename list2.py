#List-2
#Dylan and Avi
#12/8/17

from random import *

def main():
    num = []
    odds = []
    even = []
    for i in range(20):
        nums = randint(1, 100)
        num.append(nums)
    for i in num:
        if i%2 != 0.0:
            odds.append(i)
        else:
            even.append(i)
    even.sort()
    odds.sort()
    print "These are the odd number of the list: ", odds
    print "\n This is the highest even number of the list: ", max(even)

main()
