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
    return strengths_sum


with open("input/10.txt","r") as f:
    print(execute(f.read().splitlines()))