def setMatrixZeros(nums):
    rows,cols = len(nums),len(nums[0])
    iscolzero = [False for i in range(cols)]
    isrowzero = [False for i in range(rows)]
    #   . . . .
    # x[1,1,1,0]
    # x[0,1,1,0]
    # x[. . . .]
    for r in range(rows):
        for c in range(cols):
            if nums[r][c] ==0:
                iscolzero[c]=True
                isrowzero[r]=True
    for i,q in enumerate(isrowzero):
        if q:
            for c in range(cols):
                nums[i][c]=0
    for i,q in enumerate(iscolzero):
        if q:
            for r in range(rows):
                nums[r][i]=0


nums = [[1,1,1],[1,0,1],[1,1,1]]
setMatrixZeros(nums)
print(nums)