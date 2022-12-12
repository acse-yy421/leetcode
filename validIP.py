

def validIP2_final(s):
    # stepSize = [1,2,3]
    # must take 3 steps to get EOStr,ie. len(ip)==4
    # stepVal <= 255
    res = []
    step_sizes = [1,2,3]
    steps = 4
    def jump(i,steps,ip):
        if steps==0 and i==len(s):
            res.append(".".join(ip[::]))
            return
        if steps==0 and i!=len(s):
            return
        if len(ip)>4:
            return       
        #compare int(s[i:i+stepsize+1]) and 255
        for ss in step_sizes:
            #check if out of bound
            if i+ss>len(s):
                continue
                
            print(int(s[i:i+ss]))
            if int(s[i:i+ss]) <= 255 and (ss==1 or s[i:i+ss][0]!="0"):
                ip.append(s[i:i+ss])
                print(ip)
                steps-=1
                jump(i+ss,steps,ip)
                #backtrack
                steps +=1
                ip.pop()

    
    jump(0,steps,[])
    print("res",res)
    return res

# s = "25525511135"
# #s="101023"
# validIP2(s)

def validIP3(s):
    # stepSize = [1,2,3]
    # must take 3 steps to get EOStr,ie. len(ip)==4
    # stepVal <= 255
    res = []
    step_sizes = [1,2,3]
    steps = 2
    def jump(i,steps,ip):
        if steps==0 and i==len(s):
            res.append(ip[::])
            return
        if steps==0 and i!=len(s):
            return
        if len(ip)>2:
            return       
        #compare int(s[i:i+stepsize+1]) and 255
        for ss in step_sizes:
            if int(s[i:i+ss]) <= 255:
                ip.append(s[i:i+ss])
                print(ip)
                steps-=1
                jump(i+ss,steps,ip)
                #backtrack
                steps +=1
                ip.pop()
                #jump(i,steps,ip)
    
    jump(0,steps,[])
    print("res",res)
    return res

# s = "12255"
# validIP3(s)

s = "0124"
print(int(s))
