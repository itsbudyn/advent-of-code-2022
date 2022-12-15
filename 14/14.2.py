import re

def sand(s):
    width_buffer  = 1
    widths,heights=[],[]
    for i in s:
        fetched=re.findall(r"\d*,\d*",i)
        if fetched:
            for i in fetched:
                numbers=i.split(",")
                widths.append(int(numbers[0]))
                heights.append(int(numbers[1]))

    widths=sorted(widths)
    heights=sorted(heights)

    width  = widths[-1]//2
    height = 3 + heights[-1]

    offset=widths[0]-width_buffer*128
    pouring_point=500-widths[0]+width_buffer*128

    del widths
    del heights

    cave = [["."]*width*2 for i in range(height)]
    for i in range(len(cave[0])): cave[-1][i]="#"

    for instruction in s:
        points=instruction.split("->")
        for i in range(len(points)-1):
            point_1=points[i].split(",")
            point_2=points[i+1].split(",")
            if int(point_1[0])==int(point_2[0]):
                step=1 if int(point_2[1]) > int(point_1[1]) else -1
                for j in range(int(point_1[1]),int(point_2[1]) + step,step): cave[j][int(point_1[0])-offset]="#"
            elif int(point_1[1])==int(point_2[1]):
                step=1 if int(point_2[0]) > int(point_1[0]) else -1
                for j in range(int(point_1[0]),int(point_2[0]) + step,step): cave[int(point_1[1])][j-offset]="#"

    in_void=False
    drops=0

    while not in_void:
        sandpos=[0,pouring_point]
        if cave[sandpos[0]][sandpos[1]]=="o": break
        for i in range(height):
            if sandpos[0]+i+1>=height:
                in_void=True
                break

            if cave[sandpos[0]+i+1][sandpos[1]] in "#o":
                if cave[sandpos[0]+i+1][sandpos[1]-1] in "#o" and cave[sandpos[0]+i+1][sandpos[1]+1] in "#o":
                    cave[sandpos[0]+i][sandpos[1]]="o"
                    break
                elif cave[sandpos[0]+i+1][sandpos[1]-1]==".": sandpos[1]-=1
                elif cave[sandpos[0]+i+1][sandpos[1]+1]==".": sandpos[1]+=1

        if not in_void: drops+=1

    for i in cave:
        for j in i: print(j,end="")
        print()
    return drops

with open("14/14.txt","r") as f:
    print(sand(f.read().splitlines()))