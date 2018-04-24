def sieve(n):
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False
    answer = []
    for prime in range(n+1):
        if isPrime[prime]:
            answer.append(prime)
            for multiples in range(2*prime, n+1, prime):
                isPrime[multiples] == False
    return answer
def lockerProblem(lockers):
        isOpen = [False] * (lockers + 1) 
        students = lockers
        for student in range(1, students+1):
            for locker in range(student, lockers+1, student):
                isOpen[locker] = not isOpen[locker]
        openLockers = [] 
        for locker in range(1, lockers+1):
            if isOpen[locker]:
                openLockers.append(locker)
        return openLockers
