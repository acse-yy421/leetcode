def permStr(s1,s2):
    if len(s1)>len(s2):
        return False
    perms = []
    perm = []
    cnt = {l:0 for l in s1}
    for l in s1:
        cnt[l]+=1
    def dfs():
        if len(perm)==len(s1):
            perms.append(perm[::])
            return
        for l in cnt:
            if cnt[l]>0:
                perm.append(l)
                cnt[l]-=1
                dfs()
                perm.pop()
                cnt[l]+=1
    dfs()
    print("perms:",perms)
    joinedperms = []
    for _ in perms:
        joinedperms.append("".join(_))
    print(joinedperms)
    for perm in joinedperms:
        l,r = 0,0+len(s1)
        while True and r<=len(s2):
            print("s2",s2[l:r])
            if perm == s2[l:r]:
                return True
            l+=1
            r+=1
            
    return False
print(permStr("trinitrophenylmethylnitramine","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdcda"))