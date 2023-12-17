def solution(n):
    calcTable = [1] + [0] * (n)

    for brickHeights in range(1, n + 1):
        for stairHeight in range(n, brickHeights - 1, -1):
            calcTable[stairHeight] += calcTable[stairHeight - brickHeights]

    return calcTable[-1] - 1

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(100))
print(solution(200))
