def execute(s:str):
    cycle=0
    x=1
    signal_strengths=[]
    for i in s:
        cycle+=1
        signal_strengths.append([cycle,x])
        if i.split(" ")[0]=="addx":
            cycle+=1
            signal_strengths.append([cycle,x])
            x+=int(i.split(" ")[1])

    strengths_sum=0
    for i in signal_strengths:
        if i[0] in [20,60,100,140,180,220]: strengths_sum+=i[0]*i[1]

    screen=[[" "]*40 for i in range(6)]

    for i in range(signal_strengths[-1][0]):
        if abs(i%40-signal_strengths[i][1])<2: screen[i//40][i%40]="█"

    return screen

with open("10.txt","r") as f:
    for i in execute(f.read().splitlines()):
        for j in i: print(j,end="\0")
        print("")