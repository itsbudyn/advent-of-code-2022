def rock_paper_scissors(opponent:str,player:str):
    if opponent==player: return None
    match opponent:
        case "Rock":
            match player:
                case "Paper":
                    return True
                case "Scissors":
                    return False
        case "Paper":
            match player:
                case "Rock":
                    return False
                case "Scissors":
                    return True
        case "Scissors":
            match player:
                case "Rock":
                    return True
                case "Paper":
                    return False

opponent_moves={"A":"Rock","B":"Paper","C":"Scissors"}

points={
    "Rock":1,"Paper":2,"Scissors":3,
    False:0,None:3,True:6
}

outcomes={
    "X":False,"Y":None,"Z":True
}

def game(g:str):
    score=0
    for i in g:
        for j in points.keys():
            if rock_paper_scissors(opponent_moves[i[0]],j)==outcomes[i[2]]:
                score+=points[j]+points[outcomes[i[2]]]
                break
    return score

with open("input/2.txt","r") as f:
    print(game(f.read().splitlines()))