def visibleTrees(s:str):
    treemap=[[None]*len(s) for i in range(len(s))]
    visible=[[0]*len(s) for i in range(len(s))]
    for i in range(len(treemap)):
        for j in range(len(treemap)):
            treemap[i][j]=int(s[i][j])

    for i in treemap: print(i)

    for i in range(len(treemap)):
        visible[0][i]=1
        visible[-1][i]=1
        visible[i][0]=1
        visible[i][-1]=1

    for i in range(len(treemap)-1): #RIGHT
        height=treemap[i][0]
        for j in range(len(treemap)-1):
            if height < treemap[i][j+1]: 
                visible[i][j+1]=1
                height=treemap[i][j+1]

    for i in range(len(treemap)-1): #DOWN
        height=treemap[0][i]
        for j in range(len(treemap)-1):
            if height < treemap[j+1][i]:
                visible[j+1][i]=1
                height=treemap[j+1][i]

    for i in range(-1,-len(treemap),-1): #LEFT
        height=treemap[i][-1]
        for j in range(-1,-len(treemap),-1):
            if height < treemap[i][j-1]:
                visible[i][j-1]=1
                height=treemap[i][j-1]

    for i in range(-1,-len(treemap),-1): #UP
        height=treemap[-1][i]
        for j in range(-1,-len(treemap),-1):
            if height < treemap[j-1][i]: 
                visible[j-1][i]=1
                height=treemap[j-1][i]

    visibleTrees=0
    for i in visible:
        for j in i:
            if j: visibleTrees+=1

    print(" ")
    for i in visible: print(i)
    return visibleTrees


with open("8.txt","r") as f:
    print(visibleTrees(f.read().splitlines()))