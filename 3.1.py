abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rucksack(s:str):
    sum=0
    groups=[]
    group=""
    for i in s:
        j=i[:len(i)//2]
        k=i[len(i)//2:]
        for l in j:
            if l in k: 
                sum+=abc.index(l)+1
                break
    return sum

with open("input/3.txt","r") as f:
    print(rucksack(f.read().splitlines()))