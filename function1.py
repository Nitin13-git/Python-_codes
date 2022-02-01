#matrix  multiplication
p=[] 
dim=len(u)
for i in range(dim):
    for j in range(dim):
        p.append([0])
print(p)

def dot_product(v,u):
    ans=0
    for i in range(len(v)):
        ans=ans+u[i]*v[i]
    return ans
print(dot_product(u,v))

