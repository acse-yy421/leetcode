def combination_sum(nums,target):
    comb = []
    #nums = [2,3,6,7], target= 7

    def dfs(i,cur,tot):
        if tot==target:
            comb.append(cur[::])
            return
        if tot>target or i>=len(nums):
            return
        
        cur.append(nums[i])
        dfs(i,cur,tot+nums[i])
        cur.pop()
        dfs(i+1,cur,tot)

    dfs(0,[],0)

    return comb

nums=[2,3,6,7]
print(combination_sum(nums,7))




