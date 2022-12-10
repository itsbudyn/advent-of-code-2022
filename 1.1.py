def elves(calories:str):
    calories+="\n"
    elves_calories=[]
    calories=calories.split("\n")
    cal=0
    for i in calories:
        if i: cal+=int(i)
        else:
            elves_calories.append(cal)
            cal=0

    print("WYNIK:",sorted(elves_calories)[-1])
    print("WWNIK 2:",sum(sorted(elves_calories)[-3::]))

with open("1.txt","r") as f:
    elves(f.read())