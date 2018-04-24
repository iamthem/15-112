# Leandro Lopez

# lslopez, mkchan, xuliangs (groupmates)

# Section H

'''
I
1) slow1() finds the length of a list nondestructively by popping one item at
a time in a while loop
2) Since the while loop will iterate until the list is empty, the runtime will
be O(N) where N is the length of the list. 
3) 
def slow1(a):
	return len(a) 
4) The runtime of len(a) is O(1) because when the list is created,
 the length is embedded to it as a characteristic. 
 Referencing is constant time. 

II
1) slow2() returns true if the items in the list are unique. If there are any 
repeated items in the list, it will return false.
2) Its runtime is O(N**2) since it takes n**2 steps to run through both 
for loops and the equivalence check is in constant time.
3) 
def slow2(a): 
	return len(set(a)) == len(a)
4)O(N) because of the sorted builtin function. set() is linear time and it
 is added to O(1), however it remains the same parent function.  

III
1) slow3() returns the unique elements that are in b but not a
2) Its runtime is O(N**2) since it does a for loop (O(N)) 
and in every for loop it checks membership (O(N)), 
thereby making it O(N**2)
3)
def slow3(a,b):
	countsA, countsB, n, result = dict(), dict(), len(a), 0
	for i in range(len(a)):
		countA = 1 + countsA.get(a[i], 0)
		countB = 1 + countsB.get(b[i], 0)
		countsA[a[i]], countsB[b[i]] = countA, countB
	for keys in countsB:
		if keys not in countsA.keys():
			result += countsB[keys]
	return result
4) Complexity O(N) since checking membership in dictionaries and 
sets is constant time and iterating on a for loop is linear time

IV
1) slow4() finds the largest absolute difference between values of two lists
with the same length.
2) Complexity of O(N**2) since it takes n**2 steps to run through the nested 
for loops. 
3) 
def slow4(a,b):
	n = len(a)
	assert(n == len(b))
	return max(abs(max(a)-min(b)), abs(min(a)-max(b)))
4)Complexity of O(N) because max and min functions are linear time while abs is 
constant time 


V
1) slow5() finds the mininum difference between values of two lists 
2) It has complexity of O(N**2) since it takes n**2 steps to run thorugh the 
nested for loops
'''

##############
# Lab 7
##############
import cs112_f17_week7_linter

# Sort list and add largest two items, else return none 
def largestSumOfPairs(a): 
	return sorted(a)[-1] + sorted(a)[-2] if len(a)>1 else None #nlogn


# Finds triples using sets and lists
def containsPythagoreanTriple(a):
	#make list of squares 	
	squares, subtraction = sorted([x**2 for x in a]), 0 #O(N)  
	setSquares = set(squares) #make set of squares
	#iterate backwards through list of squares and 
	#check if their substraction is in the list of squares	
	for i in range(len(squares)-1, 1, -1):  #O(N)		
		subtraction = squares[i] - squares[i-1]  
		if subtraction in setSquares: return True #O(1) 
	return False	
	
def main():
    cs112_f17_week7_linter.lint() # check style rules

if __name__ == '__main__':
    main()   







