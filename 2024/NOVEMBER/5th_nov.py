# rotate by 90

m=[[1, 2, 3], [4, 5, 6], [7 ,8 ,9]]

def rotate(m):
    n=len(m)

    for i in range(n):
        for j in range(i+1,n):
            m[i][j],m[j][i]=m[j][i],m[i][j]

    for i in range(n):
        m[i].reverse()

    for i in range(n):
        for j in range(n):
            print(m[i][j],end=" ")

        print()

rotate(m)