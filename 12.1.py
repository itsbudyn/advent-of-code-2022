def path(s):
    startpos = [None,None]
    visited = []

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "S":
                startpos=[i,j]
                break

    paths = [[startpos]]

    s[startpos[0]][startpos[1]]="a"

    while True:
        current_paths=[]
        for i in range(len(paths)):
            curr_x=paths[i][-1][1]
            curr_y=paths[i][-1][0]

            height=ord(s[curr_y][curr_x])

            if curr_y+1 < len(s) and height + 1 >= ord(s[curr_y+1][curr_x]) and [curr_y+1,curr_x] not in paths[i]: #DOWN
                if height==ord("z") and s[curr_y+1][curr_x]=="E": return paths[i]
                if [curr_y+1,curr_x] not in visited:
                    current_paths.append(paths[i]+[[curr_y+1,curr_x]])
                    visited.append([curr_y+1,curr_x])

            if curr_y > 0 and height + 1 >= ord(s[curr_y-1][curr_x]) and [curr_y-1,curr_x] not in paths[i]: #UP
                if height==ord("z") and s[curr_y-1][curr_x]=="E": return paths[i]
                if [curr_y-1,curr_x] not in visited:
                    current_paths.append(paths[i]+[[curr_y-1,curr_x]])
                    visited.append([curr_y-1,curr_x])

            if curr_x+1 < len(s[0]) and height + 1 >= ord(s[curr_y][curr_x+1]) and [curr_y,curr_x+1] not in paths[i]: #RIGHT
                if height==ord("z") and s[curr_y][curr_x+1]=="E": return paths[i]
                if [curr_y,curr_x+1] not in visited:
                    current_paths.append(paths[i]+[[curr_y,curr_x+1]])
                    visited.append([curr_y,curr_x+1])

            if curr_x > 0 and height + 1 >= ord(s[curr_y][curr_x-1]) and [curr_y,curr_x-1] not in paths[i]: #LEFT
                if height==ord("z") and s[curr_y][curr_x-1]=="E": return paths[i]
                if [curr_y,curr_x-1] not in visited:                
                    current_paths.append(paths[i]+[[curr_y,curr_x-1]])
                    visited.append([curr_y,curr_x-1])

        paths=current_paths

with open("input/12.txt","r") as f:
    print(len(path(list([i for i in j] for j in f.read().splitlines()))))