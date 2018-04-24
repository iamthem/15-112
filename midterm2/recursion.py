import os 
def countFiles(path):
    if os.path.isfile(path):
        return 1
    count = 0 
    for item in os.listdir(path):
        newPath = path + '/' + item
        count += countFiles(newPath)
    return count

def increasingPathCountHelper(board, i, j):
    if i == len(board)-1 and j == len(board)-1: return 1 
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    count = 0
    for m, n in moves: 
        if ((0 <= i+m < len(board)) and (0 <= j+n < len(board[0])) and 
                (board[i+m][j+n] > board[i][j])):
            solution = increasingPathCountHelper(board, i+m, j+n)
            if solution != None: count += solution
    return count                    

def increasingPathCount(board):
    return increasingPathCountHelper(board, 0,0)

def containsCopies(path, tmpFile = ''):
    if os.path.isfile(path):
        f = open(path, "r")
        if f.read() == tmpFile: return True
    else: 
        for item in os.listdir(path):
            newpath = os.path.join(path, item)
            if os.path.isfile(newpath) and tmpFile == "": 
                f = open(path, "r") 
                tmpFile = f.read()
                solution = containsCopies(path, tmpFile)
                if solution != None: return solution 
                else: tmpFile = ""
            else: containsCopies(newpath, tmpFile)

def pairsSum(a, s, currL = []):
    if isDone(a, s, currL): return currL
    for i, v in enumerate(a):
        guess = checkPairs(s, i, a)
        if guess:
                currL.append((v, guess[0]))
                a.remove(v)
                a.remove(guess[0])
                solution = pairsSum(a,s,currL)
                if solution != None: return solution
                else: 
                    currL.pop()
                    a.insert(v, i) 
                    a.insert(guess[0], guess[1])
    return None 

def isDone(a,s,currL):
    if len(currL) != len(a)//2: return False
    for i,j in currL:
        if i+j > s: return False
    return True

def checkPairs(s, i, a):
    for j in range(len(a)):
        if ((a[i] + a[j] <= s and i != j) or 
             (a[i] + a[j] <= s and a[i] == a[j] and i != j)): return a[j], j
    return None 

def wordLadderHelper(L, start, target, currL):
    if currL[-1] == target: return currL
    print(currL)
    for i, word in enumerate(L): 
        if checkDistance(word, currL): 
            currL.append(word)
            L.pop(i)
            solution = wordLadderHelper(L, start, target, currL)
            print(currL)
            if solution != None: return solution 
            else:
                currL.pop()
                L.insert(i, word)
    return None 

def wordLadder(L, start, target):
    currL = [start] 
    L.remove(start)
    return wordLadderHelper(L, start, target, currL)

def checkDistance(word, currL):
    distance = 0
    for i in range(len(word)):
        if word[i] != currL[-1][i]: distance += 1
    return distance == 1







