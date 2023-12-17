def solution(l, t):
    currentT = 0
    startIndex = 0

    for endIndex, v in enumerate(l):
        currentT = currentT + v

        while(currentT > t and endIndex > startIndex ):
            currentT = currentT - l[startIndex]
            startIndex += 1

        if currentT == t:
            return [startIndex, endIndex]

    return [-1,-1]
