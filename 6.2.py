with open("6.txt","r") as f:
    buffer=f.read()

cutoff=0

for i in range(len(buffer)-4):
    unique=True
    for j in buffer[i:i+4]:
        if buffer[i:i+4].count(j)>1:
            unique=False
            break
    if unique: 
        print(buffer)
        print(buffer[0:i+4])
        cutoff=len(buffer[:i+4])
        buffer=buffer[i+4:]
        print(buffer)
        break

for i in range(len(buffer)-14):
    unique=True
    for j in buffer[i:i+14]:
        if buffer[i:i+14].count(j)>1:
            unique=False
            break
    if unique: 
        print(cutoff+i+14)
        break
