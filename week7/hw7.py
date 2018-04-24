####################
# Leandro Lopez
# lslopez
# Section H
###################
#################################################
# Hw7
#################################################

import cs112_f17_week7_linter
import time 
import random
import copy

#inverts dictionary using set union
def invertDictionary(d):
	answer = dict()
	#iterate over key,value tuples
	for item in d.items(): #O(N)
		#Use set union to append items to answer[item[1]]
		if item[1] in answer: answer[item[1]] |= set([item[0]])
		else: answer[item[1]] = set([item[0]])
	return answer

# Finds fof using set union and difference, O(N**2)
def friendsOfFriends(d):
	answer = dict()
	#iterate over key,value tuples
	for item in d.items(): 
		# If person has no friends, no fof :(
		if not item[1]: answer[item[0]] = item[1]
		#iterate over list of names 
		for name in list(item[1]):
			#Use set union and difference find fof	
			if item[0] in answer:
				union = answer[item[0]] | d[name]				
				answer[item[0]] = union - d[item[0]]		
			else: answer[item[0]] = d[name] - d[item[0]]
		#Remove person's own name 
		if item[0] in answer[item[0]]: answer[item[0]].remove(item[0])	
	return answer	

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])


def instrumentedSelectionSort(a):
	t0, tf, dt, comps, swaps = 0, 0, 0, 0, 0 #initialize relevant variables	
	t0 = time.time()	
	n = len(a)
	for startIndex in range(n):
		minIndex = startIndex
		for i in range(startIndex+1, n):
			comps += 1     # add comparison 		
			if (a[i] < a[minIndex]):
                		minIndex = i 
		swap(a, startIndex, minIndex)
		swaps += 1      # add time
	tf = time.time()
	dt = tf - t0	#measure time
	return (comps, swaps, dt)

def instrumentedBubbleSort(a):
	t0, tf, dt, comps, swaps = 0, 0, 0, 0, 0 #initialize relevant variables
	t0 = time.time()	
	c = copy.deepcopy(a)	
	n = len(a)
	end = n
	swapped = True 
	while (swapped):
		swapped = False
		for i in range(1, end):
			comps += 1 # add comparison 
			if (c[i-1] > c[i]):
				swap(c, i-1, i)
				swapped = True 			
				swaps += 1 #add swap 
		end -=1

	tf = time.time()
	dt = tf - t0
	return (comps, swaps, dt)

def printMins(triple):
	# Print report outlining best time, swaps and comparisons
	answers = ['Selection sort finishes with less',
	           'Bubble sort finishes with less']
	if min(triple[:2]) == triple[0]:
		print(answers[1], triple[2])
	else: print(answers[0], triple[2])
		

def selectionSortVersusBubbleSort(): 
	# Initialize relevant variables	
	selecaddSwaps, selecaddComps, selecaddTimes = 0, 0, 0
	bubbleaddSwaps, bubbleaddComps, bubbleaddTimes = 0, 0, 0
	# Do test 10 times for empirical certainty 
	for i in range(10):
		# Do tests and add values to relevant variables	
		b = [random.randint(0,2**31) for i in range(2**10)]
		selecaddSwaps += instrumentedSelectionSort(b)[1]
		selecaddComps += instrumentedSelectionSort(b)[0]
		selecaddTimes += instrumentedSelectionSort(b)[2]
		b = [random.randint(0,2**31) for i in range(2**10)]
		bubbleaddComps += instrumentedBubbleSort(b)[0]
		b = [random.randint(0,2**31) for i in range(2**10)]
		bubbleaddSwaps += instrumentedBubbleSort(b)[1]
		b = [random.randint(0,2**31) for i in range(2**10)]		
		bubbleaddTimes += instrumentedBubbleSort(b)[2]
		n = len(b)
	# Take averages and print 
	print("%10s swaps=%d comparisons=%d  time=%6.3fs" % ('Selection Sort', 
        selecaddSwaps / 3, selecaddComps / 3, selecaddTimes / 3))
	print("%10s swaps=%d comparisons=%d  time=%6.3fs" % ('Bubble Sort', 
        bubbleaddSwaps / 3, bubbleaddComps / 3, bubbleaddTimes / 3))
	# Take big O	
	print("Selection sort is O(%6.3fn**2 )" % ((selecaddComps / 3)/(n**2)))	
	print("Bubble sort is O(%6.3fn**2 )" % ((bubbleaddComps / 3)/(n**2)))
	#iterate through different computational variables to find min 	
	for i in [(bubbleaddComps, selecaddComps, 'comparisons'), 
		(bubbleaddSwaps, selecaddSwaps, 'swaps'), 
		(bubbleaddTimes, selecaddTimes, 'time')]:
		printMins(i)	

###########################
# Test Functions 
###########################

def testInvertDictionary():
    print('Testing invertDictionary()... ', end='')
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
       {2:set([1]), 3:set([2,5]), 4:set([3])})
    assert(invertDictionary({1:'Foo', 2:3, 'spam': 'eggs', 5:40, 'a':'Foo'})==
       {40: {5}, 'eggs': {'spam'}, 3: {2}, 'Foo': {1, 'a'}})
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3, 'a':-1, 'b': 3}) == 
	   {2: {1}, 3: {'b', 2, 5}, 4: {3}, -1: {'a'}})
    assert(invertDictionary({1:2, 2:2, 3:2, 4:2}) == {2: {1, 2, 3, 4}})
    print('Passed!')
def testFof():
	print('Testing invertDictionary()... ', end='')
	d = dict()
	d["jon"] = set(["arya", "tyrion"])
	d["tyrion"] = set(["jon", "jaime", "pod"])
	d["arya"] = set(["jon"])
	d["jaime"] = set(["tyrion", "brienne"])
	d["brienne"] = set(["jaime", "pod"])
	d["pod"] = set(["tyrion", "brienne", "jaime"])
	d["ramsay"] = set()
	answer = {
	'tyrion': {'arya', 'brienne'}, 
	'pod': {'jon'}, 
	'brienne': {'tyrion'}, 
	'arya': {'tyrion'}, 
	'jon': {'pod', 'jaime'}, 
	'jaime': {'pod', 'jon'}, 
	'ramsay': set()
	}
	assert(friendsOfFriends(d) == answer)
	print('Passed!')


def main():
    cs112_f17_week7_linter.lint() # check style rules

if __name__ == '__main__':
    main()   
