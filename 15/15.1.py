import re

def beacons(s):
    sensor_arr,beacon_arr=[],[]
    for i in s:
        numbers=re.findall(r"[-]*\d*",i)
        n_arr=[]
        for j in numbers: n_arr.append(j) if j else None
        sensor=[int(n_arr[1]),int(n_arr[0])]
        beacon=[int(n_arr[3]),int(n_arr[2])]
        sensor_arr.append(sensor) if sensor not in sensor_arr else None
        beacon_arr.append(beacon) if beacon not in beacon_arr else None

    sensor_arr=sorted(sensor_arr,key=lambda x:int(x[0]))
    beacon_arr=sorted(beacon_arr,key=lambda x:int(x[0]))

    height = max(sensor_arr[-1][0],beacon_arr[-1][0])

    h_offset = min(sensor_arr[0][0],beacon_arr[0][0])
    h_offset = abs(h_offset) if h_offset < 0 else 0

    sensor_arr=sorted(sensor_arr,key=lambda x:int(x[1]))
    beacon_arr=sorted(beacon_arr,key=lambda x:int(x[1]))

    width = max(sensor_arr[-1][1],beacon_arr[-1][1])

    w_offset = min(sensor_arr[0][1],beacon_arr[0][1])
    w_offset = abs(w_offset) if w_offset < 0 else 0

    height+=h_offset+1
    width+=w_offset+1

    print(height,width)

    radar=[["." for i in range(width)] for j in range(height)]
    print("DONE")

    for i in sensor_arr: 
        radar[i[0]+h_offset][i[1]+w_offset]="S"
    for i in beacon_arr: 
        print(i,i[0]+h_offset,i[1]+w_offset)
        radar[i[0]+h_offset][i[1]+w_offset]="B"

    for i in sensor_arr:
        print(i)
        found=False
        paths=[[[i[0]+h_offset,i[1]+w_offset]]]
        visited=[]
        while not found:
            current_paths=[]
            for j in range(len(paths)):
                curr_x=paths[j][-1][1]
                curr_y=paths[j][-1][0]

                if curr_y+1 < height:
                    if [curr_y+1,curr_x] not in visited:
                        current_paths.append([[curr_y+1,curr_x]])
                        visited.append([curr_y+1,curr_x])
                        match radar[curr_y+1][curr_x]:
                            case ".": radar[curr_y+1][curr_x]="#"
                            case "B": found=True
                if curr_y > 0:
                    if [curr_y-1,curr_x] not in visited:
                        current_paths.append([[curr_y-1,curr_x]])
                        visited.append([curr_y-1,curr_x])
                        match radar[curr_y-1][curr_x]:
                            case ".": radar[curr_y-1][curr_x]="#"
                            case "B": found=True
                if curr_x+1 < width:
                    if [curr_y,curr_x+1] not in visited:
                        current_paths.append([[curr_y,curr_x+1]])
                        visited.append([curr_y,curr_x+1])
                        match radar[curr_y][curr_x+1]:
                            case ".": radar[curr_y][curr_x+1]="#"
                            case "B": found=True
                if curr_x > 0:
                    if [curr_y,curr_x-1] not in visited:
                        current_paths.append([[curr_y,curr_x-1]])
                        visited.append([curr_y,curr_x-1])
                        match radar[curr_y][curr_x-1]:
                            case ".": radar[curr_y][curr_x-1]="#"
                            case "B": found=True
            if True:           
                for x in radar:
                    for y in x: print(y,end="")
                    print()
                print()

            paths=current_paths

with open("15/15.txt","r") as f:
    print(beacons(f.read().splitlines()))