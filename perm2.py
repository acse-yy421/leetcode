def perm2(nums):
    #[1,1,2] -> [[1,1,2],[2,1,1],[1,2,1]]
    res = []
    perm = []
    count = {c:0 for c in nums}
    for c in nums:
        count[c]+=1
    def dfs():
        if len(perm)==len(nums):
            res.append(perm[::])
            return
        for num in count:
            if count[num]>0:
                perm.append(num)
                count[num]-=1
                dfs()
                perm.pop()
                count[num]+=1
    dfs()
    return res

nums = [1,1,2]
print(perm2(nums))




        
