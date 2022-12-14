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
    indices_sum=0

    for i in s: 
        if i: pairs.append(eval(i))

    for i in range(0,len(pairs)-1,2):
        if sigcmp(pairs[i],pairs[i+1]): indices_sum+=(i//2)+1
    return indices_sum

with open("13/13.txt","r") as f:
    print(distress(f.read().splitlines()))