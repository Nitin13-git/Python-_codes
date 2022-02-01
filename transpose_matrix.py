def transpose(mat):
    m=len(mat)
    n=len(mat[0])
    mat_trans=[]
    for i in range(n):
        t=[]
        for j in range(m):
            t.append(mat[j][i])
        mat_trans.append(t)
    return(mat_trans)