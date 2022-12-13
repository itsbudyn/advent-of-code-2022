with open("input/6.txt","r") as f:
    buffer=f.read()

for i in range(len(buffer)-4):
    unique=True
    for j in buffer[i:i+4]:
        if buffer[i:i+4].count(j)>1:
            unique=False
            break
    if unique: 
        print(i+4)
        break
