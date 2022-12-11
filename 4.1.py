def camp(s:int):
    matches=0
    for i in range(len(s)): s[i]=s[i].split(",")
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j]=s[i][j].split("-")
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j][0]=int(s[i][j][0])   
            s[i][j][1]=int(s[i][j][1])       
    for i in s:
        if (i[0][0] >= i[1][0] and i[0][1] <= i[1][1]) or (i[0][0] <= i[1][0] and i[0][1] >= i[1][1]):
            matches+=1
    return matches

with open("input/4.txt","r") as f:
    print(camp(f.read().splitlines()))