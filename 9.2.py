def bridge(s:str):
    x=[1,1]
    y=[1,1]
    for line in s:
        instruction=line.split(" ")
        match instruction[0]:
            case "L": x[0]+=int(instruction[1])
            case "R": x[1]+=int(instruction[1])
            case "D": y[0]+=int(instruction[1])
            case "U": y[1]+=int(instruction[1])

    grid=[[" "]*sorted(x)[1] for y in range(sorted(y)[1])]
    rope_visited=[[" "]*sorted(x)[1] for y in range(sorted(y)[1])]
    rope_tail_visited=[[" "]*sorted(x)[1] for y in range(sorted(y)[1])]
    startpos=[sorted(y)[1]//2,sorted(x)[1]//2]
    headpos=startpos
    tailpos=[None,None]
    lastheadpos=[None,None]

    for line in s:
        instruction=line.split(" ")

        for i in range(int(instruction[1])):
            lastheadpos=[headpos[0],headpos[1]]
            grid[headpos[0]][headpos[1]]=" "
            match instruction[0]:
                case "L": 
                    grid[headpos[0]][headpos[1]-1]="H"
                    headpos[1]-=1
                case "R": 
                    grid[headpos[0]][headpos[1]+1]="H"
                    headpos[1]+=1
                case "D": 
                    grid[headpos[0]+1][headpos[1]]="H"
                    headpos[0]+=1
                case "U": 
                    grid[headpos[0]-1][headpos[1]]="H"
                    headpos[0]-=1
            headDetached=True
            if tailpos[0]==None or tailpos[1]==None:
                tailpos=lastheadpos
                rope_visited[tailpos[0]][tailpos[1]]="9"
                headDetached=False
            else:
                for j in range(tailpos[0]-1,tailpos[0]+2):
                    for k in range(tailpos[1]-1,tailpos[1]+2):
                        try:
                            if grid[j][k]=="H":
                                headDetached=False
                                break
                        except IndexError: pass
                    if not headDetached: break
            if headDetached:
                tailpos=lastheadpos
                rope_visited[lastheadpos[0]][lastheadpos[1]]="9"

        for i in rope_visited: print(i)

    visited=0
    for i in rope_visited:
        for j in i:
            if j=="T": visited+=1
    return visited

with open("9.txt","r") as f:
    print(bridge(f.read().splitlines()))