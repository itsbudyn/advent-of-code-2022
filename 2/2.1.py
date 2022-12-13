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

player_moves_1={"X":"Rock","Y":"Paper","Z":"Scissors"}
player_moves_2={"X":"Rock","Y":"Scissors","Z":"Paper"}
player_moves_3={"X":"Paper","Y":"Rock","Z":"Scissors"}
player_moves_4={"X":"Paper","Y":"Scissors","Z":"Rock"}
player_moves_5={"X":"Scissors","Y":"Rock","Z":"Paper"}
player_moves_6={"X":"Scissors","Y":"Paper","Z":"Rock"}

moves=[player_moves_1,player_moves_2,player_moves_3,player_moves_4,player_moves_5,player_moves_6]

points={
    "Rock":1,"Paper":2,"Scissors":3
}

def game(g:str):
    scores=[]
    for i in moves:
        score=0
        for j in g:
            match rock_paper_scissors(opponent_moves[j[0]],i[j[2]]):
                case None: score+=3
                case True: score+=6
            score+=points[i[j[2]]]
        scores.append(score)
    print(sorted(scores))
    
    return sorted(scores)[-1]

with open("input/2.txt","r") as f:
    print(game(f.read().splitlines()))