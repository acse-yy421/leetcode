def perm(nums):
    #[1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
    res = []
    if len(nums)==1:
        return [nums]
    for e in nums:
        remainingElements = [a for a in nums if e!=a] #get all the elements except for itself
        sub_perm = perm(remainingElements)
        for t in sub_perm:
            res.append(t+[e])

    
    return res

print(perm([1,2,3,4]))