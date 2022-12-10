def camp(s:int):
    overlaps=0
    for i in range(len(s)): s[i]=s[i].split(",")
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j]=s[i][j].split("-")
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j][0]=int(s[i][j][0])   
            s[i][j][1]=int(s[i][j][1])       
    for i in s:
        x=list(range(i[0][0],i[0][1]+1))
        y=list(range(i[1][0],i[1][1]+1))
        for j in x:
            if j in y:
                overlaps+=1
                break
    return overlaps

with open("4.txt","r") as f:
    print(camp(f.read().splitlines()))