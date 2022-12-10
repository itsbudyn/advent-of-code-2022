def visibleTrees(s:str):
    treemap=[[None]*len(s) for i in range(len(s))]
    visible=[[0]*len(s) for i in range(len(s))]

    for i in range(len(treemap)):
        for j in range(len(treemap)):
            treemap[i][j]=int(s[i][j])

    for i in range(len(treemap)-1): #DOWN
        height=treemap[i][0]
        for j in range(len(treemap)-1):
            if height < treemap[i][j+1]: 
                visible[i][j+1]=1
                height=treemap[i][j+1]

    for i in range(len(treemap)-1): #RIGHT
        height=treemap[0][i]
        for j in range(len(treemap)-1):
            if height < treemap[j+1][i]:
                visible[j+1][i]=1
                height=treemap[j+1][i]

    for i in range(-1,-len(treemap)+1,-1): #LEFT
        height=treemap[i][-1]
        for j in range(-1,-len(treemap)+1,-1):
            if height < treemap[i][j-1]:
                visible[i][j-1]=1
                height=treemap[i][j-1]

    for i in range(-1,-len(treemap)+1,-1): #UP
        height=treemap[-1][i]
        for j in range(-1,-len(treemap)+1,-1):
            if height < treemap[j-1][i]: 
                visible[j-1][i]=1
                height=treemap[j-1][i]

    for i in range(len(visible)):
        visible[0][i]=0
        visible[-1][i]=0
        visible[i][0]=0
        visible[i][-1]=0

    visibleTrees=0
    candidates=[]
    scenic_scores=[[0]*len(s) for i in range(len(s))]
    for i in range(len(visible)):
        for j in range(len(visible)):
            if visible[i][j]:
                visibleTrees+=1
                candidates.append([i,j])

    for candidate in candidates:
        height=treemap[candidate[0]][candidate[1]]
        score=[0,0,0,0]
        for i in range(candidate[0],len(treemap)-1): #DOWN
            score[0]+=1
            if height <= treemap[i+1][candidate[1]]: break
        for i in range(candidate[1],len(treemap)-1): #RIGHT
            score[1]+=1
            if height <= treemap[candidate[0]][i+1]: break
        for i in range(candidate[0],0,-1): #UP
            score[2]+=1
            if height <= treemap[i-1][candidate[1]]: break
        for i in range(candidate[1],0,-1): #LEFT
            score[3]+=1
            if height <= treemap[candidate[0]][i-1]: break
        scenic_scores[candidate[0]][candidate[1]]=score[0]*score[1]*score[2]*score[3]
    
    maxScenicScore=0
    for i in scenic_scores:
        for j in i:
            if j>maxScenicScore: maxScenicScore=j
    return maxScenicScore

with open("8.txt","r") as f:
    print(visibleTrees(f.read().splitlines()))