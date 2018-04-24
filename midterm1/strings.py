def f(s):
    t = "CBBD"
    for i in range(4):
        print(s.count(s[i]))
        assert(s.count(s[i]) == (ord(t[i]) - ord("A")))
    return (s[::3] == s[5:2:-1])

def f1(s):
    assert (s[0] == "d" and len(s) == 5)
    for i in range(1, len(s)):
        if (ord(s[i]) != (i + ord(s[i-1]))):
            return False
    return True

def shortest(s):
    x,y = 0,0
    for c in s:
        if c == 'u': y += 1
        elif c == 'd': y -= 1
        elif c == 'r': x += 1
        elif c == 'l': x -= 1
    return len(s) == abs(x) + abs(y)

def rotateStringLeft(s,k):
    answer = ""
    for i in range(len(s)):
        answer += s[(i+k)%len(s)]
    return answer 
