abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rucksack(s:str):
    groups=[]
    group=[]
    items=""
    for i in s:
        group.append(i)
        if len(group)==3:
            groups.append(group)
            group=[]

    for i in groups:
        for j in i[0]:
            if j in i[1] and j in i[2]:
                items+=j
                break
    sum_p=0
    for i in items: 
        sum_p+=abc.index(i)+1
    return sum_p

with open("input/3.txt","r") as f:
    print(rucksack(f.read().splitlines()))