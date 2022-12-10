from re import findall

stacks=[
    ["N","C","R","T","M","Z","P"],
    ["D","N","T","S","B","Z"],
    ["M","H","Q","R","F","C","T","G"],
    ["G","R","Z"],
    ["Z","N","R","H"],
    ["F","H","S","W","P","Z","L","D"],
    ["W","D","Z","R","C","G","M"],
    ["S","J","F","L","H","W","Z","Q"],
    ["S","Q","P","W","N"],
]

def move(s:str):
    for i in s:
        instruction=findall("[0-9]+",i)
        for i in range(len(instruction)):
            instruction[i]=int(instruction[i])-1
        instruction[0]+=1

        for j in range(instruction[0]):
            stacks[instruction[2]].append(stacks[instruction[1]][-1])
            del stacks[instruction[1]][-1]
        
    out=""
    for i in stacks: out+=i[-1] if i else None
    return out


with open("5.txt","r") as f:
    print(move(f.read().splitlines()))