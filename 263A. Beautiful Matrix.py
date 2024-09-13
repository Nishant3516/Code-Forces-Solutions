def getOnePosition(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==1:
                return [i,j]

def getMoves(matrix):
    onePosition=getOnePosition(matrix)
    return abs(onePosition[0]-2)+abs(onePosition[1]-2)


matrix=[]
for i in range(5):
    matrix.append(list(map(int, input().split())))
print(getMoves(matrix))