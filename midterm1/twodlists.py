def rotatingListClockwise(L):
    M = []
    A = []
    rows, cols = len(L), len(L[0])
    for i in range(cols):
        for j in range(rows):
            M.append(L[j][i])
        A.append(M)
        M = []
    return A

def rotatingListCounterClokwise(L):
    M = [] 
    A = []
    rows, cols = len(L), len(L[0])
    for i in range(cols-1, -1, -1):
        for j in range(rows):
            M.append(L[j][i])
        A.append(M)
        M = []
    return A


