l=['nitin','nandani','deeksha',"danish",'nitin','nandani','deeksha',"danish"]
s=set(l)
d={}
for x in s:
    d[x]=0
print(s)
for x in l:
    d[x]=d[x]+1
print(d)
