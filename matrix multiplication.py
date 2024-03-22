a=[[4,7],[3,2]]
b=[[4,3],[2,1]]
c=[[0,0],[0,0]]

print(a)
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
for i in c:
    print(i)
    
