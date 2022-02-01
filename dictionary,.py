import string 
letters=string.ascii_lowercase
data='gydsagugbnds78oywer)@#Z$%jkhreifiuilerwghuiheheiuwhfiouhhr789743259@@##9845376895bc jkvf5h7iy54c4kihiu'
l=list(data)
alpha=tuple(letters)
r=[]
for p in l:
    if p in letters:
        r.append(p)

print(r)   