# Leandro Lopez

# lslopez, arabinov (groupmate)

# Section H



#################################################

# Lab4

#################################################



import cs112_f17_week10_linter

import math, string, copy



#################################################

# Helper functions

#################################################



def almostEqual(d1, d2, epsilon=10**-7):

    # note: use math.isclose() outside 15-112 with Python version 3.5 or later

    return (abs(d2 - d1) < epsilon)



import decimal

def roundHalfUp(d):

    # Round to nearest with ties going away from zero.

    rounding = decimal.ROUND_HALF_UP

    # See other rounding options here:

    # https://docs.python.org/3/library/decimal.html#rounding-modes

    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))



#################################################

# Problems

#################################################


def areLegalValues(values):
  if math.sqrt(len(values)) % 1 != 0: return False
  else:
    for i in range(len(values)):
      if (values[i] >= 0) and (values[i] <= len(values)):
        if values[i] == 0: continue
        else:
          for j in range(len(values)):
            if j == i: continue
            elif values[i] == values[j]: return False
      else: return False
  return True



def isLegalRow(board, row):
  return areLegalValues(board[row])
  
def isLegalCol(board, col):
  colList = []
  for i in range(len(board)):
    colList += [board[i][col]]
  return areLegalValues(colList)

def isLegalBlock(board, block):
  blockLen = int(math.sqrt(len(board)))
  blockList = []
  a = (block//blockLen)*blockLen
  b = (block%blockLen)*blockLen
  for i in range(blockLen):
    blockList += board[i+a][b:b+blockLen]
  print(blockList)
  return areLegalValues(blockList)

def isLegalSudoku(board):
  n = math.sqrt(len(board))
  if n % 1 != 0: return False
  else:
    for i in range(len(board)):
      if (isLegalRow(board, i)): continue
      else: return False
    for i in range(len(board)):
      if (isLegalCol(board, i)): continue
      else: return False
    for i in range(len(board)):
      if (isLegalBlock(board, i)): continue
      else: return False
  return True
    
    
def main():
    cs112_f17_week10_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()   
