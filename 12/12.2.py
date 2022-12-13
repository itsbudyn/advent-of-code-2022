def path(s):
    startpos = [None,None]
    visited = []

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "E": 
                startpos=[i,j]
                s[i][j] = "z"

    paths = [[startpos]]
    while True:
        current_paths=[]
        for i in range(len(paths)):
            curr_x=paths[i][-1][1]
            curr_y=paths[i][-1][0]

            height=ord(s[curr_y][curr_x])

            if curr_y+1 < len(s) and (height - 1 <= ord(s[curr_y+1][curr_x])): #DOWN
                if abs(height-ord("b"))<1 and s[curr_y+1][curr_x]=="a": return paths[i]
                if [curr_y+1,curr_x] not in visited:
                    current_paths.append(paths[i]+[[curr_y+1,curr_x]])
                    visited.append([curr_y+1,curr_x])

            if curr_y > 0 and (height - 1 <= ord(s[curr_y-1][curr_x])): #UP
                if abs(height-ord("b"))<1 and s[curr_y-1][curr_x]=="a": return paths[i]
                if [curr_y-1,curr_x] not in visited:
                    current_paths.append(paths[i]+[[curr_y-1,curr_x]])
                    visited.append([curr_y-1,curr_x])

            if curr_x+1 < len(s[0]) and (height - 1 <= ord(s[curr_y][curr_x+1])): #RIGHT
                if abs(height-ord("b"))<1 and s[curr_y][curr_x+1]=="a": return paths[i]
                if [curr_y,curr_x+1] not in visited:
                    current_paths.append(paths[i]+[[curr_y,curr_x+1]])
                    visited.append([curr_y,curr_x+1])

            if curr_x > 0 and (height - 1 <= ord(s[curr_y][curr_x-1])): #LEFT
                if abs(height-ord("b"))<1 and s[curr_y][curr_x-1]=="a": return paths[i]
                if [curr_y,curr_x-1] not in visited:                
                    current_paths.append(paths[i]+[[curr_y,curr_x-1]])
                    visited.append([curr_y,curr_x-1])

        paths=current_paths

with open("input/12.txt","r") as f:
    print(len(path([[i for i in j] for j in f.read().splitlines()])))