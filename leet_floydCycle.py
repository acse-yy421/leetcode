def cycle(nums):
    # i  0,1,2,3,4    five numbers,max=4, (n+1)numbers belong to [1,n] find duplicate ones in constant space complexity and linear time complexity 
    # n [1,3,4,2,2] 
    slow,fast = 0,0
    while True:
        slow = nums[slow] # every iteration, it goes 1 step
        fast = nums[nums[fast]]#every iteration, it goes 2 steps
        if slow==fast:
            break
    slow2=0 # when fast and slow ptr meets, fast has finished its job. Start another slow ptr, because x=y, they have the step length
    while True:
        #x=y, x: the distance between where slowPtr and fastPtr meets and cycling starting point, y:distance between start point and cycling start point
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow==slow2:
            break
    return slow

print(cycle([1,3,4,2,2]))