dirsizes=[]

class File:
    def __init__(self,size:int,name:str):
        self.size=size
        self.name=name
    size=0
    name=""

class Directory:
    def __init__(self,name:str):        self.name=name
    def mkdir(self,name:str):           self.contents.append(Directory(name))
    def touch(self,size:int,name:str):  self.contents.append(File(size,name))
    
    def ls(self):
        print("Directory listing of",self.name)
        for i in self.contents:
            print(type(i),i.name,i.size)

    def ls_r(self,indentation:int=0):
        print("\t"*indentation,"Directory listing of",self.name)
        for i in self.contents:
            print("\t"*indentation," <DIR>" if type(i)==type(Directory("")) else "",i.name,i.size)
            if type(i)==type(Directory("")): 
                global dirsizes
                dirsizes.append(i.size)
                i.ls_r(indentation+1)

    def cd(self,name:str):
        for i in self.contents:
            if i.name==name: return i

    def calculateSize(self):
        for i in self.contents:
            if type(i)==type(Directory("")): i.calculateSize()
            self.size+=i.size

    name=""
    contents=[]
    size=0

def browse(s:str):
    pwd=[Directory("")]
    mode=None
    for line in s:
        if line=="$ ls": 
            mode="list"
            continue
        if "$ cd " in line: 
            mode="changedir"

        match mode:
            case "list":
                if "dir" in line: 
                    pwd[-1].mkdir(line[4:])
                    pwd[-1].cd(line[4:]).contents=[]
                else:
                    newdir=line.split(" ")
                    pwd[-1].touch(int(newdir[0]),newdir[1])

            case "changedir":
                if line=="$ cd /":      pwd=[pwd[0]]
                elif line=="$ cd ..":   pwd=pwd[:-1]
                else: pwd.append(pwd[-1].cd(line.split(" ")[2]))

    pwd[0].calculateSize()
    pwd[0].ls_r()
    dirstodel=0
    for i in dirsizes:
        if i<100000: dirstodel+=i
    print(dirstodel)

with open("input/7.txt","r") as f:
    browse(f.read().splitlines())
