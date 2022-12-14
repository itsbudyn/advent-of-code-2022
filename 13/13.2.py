import re
def sigcmp(a,b):
    if not type(a)==type([]): a=[a]
    if not type(b)==type([]): b=[b]

    longer=len(a) if len(a) >= len(b) else len(b)

    for i in range(longer):
        try: a[i]
        except IndexError: return True
        try: b[i]
        except IndexError: return False

        result=None
        if type(a[i])==type([]) or type(b[i])==type([]): result = sigcmp(a[i],b[i])
        if result != None: return result

        if a[i] != b[i]: 
            try: return a[i] < b[i]
            except TypeError: return sigcmp(a[i],b[i])

def distress(s):
    pairs=[]

    for i in s: 
        if i: pairs.append(eval(i))
        
    lessthan2=1
    lessthan6=2
    for i in pairs:
        if sigcmp(i,[[2]]): lessthan2+=1
        if sigcmp(i,[[6]]): lessthan6+=1

    return lessthan2*lessthan6

with open("13/13.txt","r") as f:
    print(distress(f.read().splitlines()))