import math

def solution(area):
    if area < 4:
        return [1] * area

    square = int(math.pow(math.floor(math.sqrt(area)), 2))

    return [square] + solution(area - square)
