import itertools

def countTimeForPath(path, times):
    time = 0

    for start, end in path:
        time += times[start][end]

    return time

def getDistanceMatrix(times):
    for i in range(len(times)):
        for j in range(len(times)):
            for k in range(len(times)):
                times[j][k] = min(times[j][k], times[j][i] + times[i][k])

    return times

def isThereNegativeCycle(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] < 0:
            return True

    return False

def constructPathForCombination(bunniesCombination):
    bunniesList = [0] + list(bunniesCombination) + [-1]

    path = []
    for i in range(1, len(bunniesList)):
        path.append((bunniesList[i - 1], bunniesList[i]))

    return path

def solution(times, time_limit):
    bunniesCount = len(times) - 2

    matrix = getDistanceMatrix(times)

    if isThereNegativeCycle(matrix):
        return list(range(0, bunniesCount))

    for savedBunniesCount in reversed(range(bunniesCount + 1)):
        for bunniesCombination in itertools.permutations(range(1, bunniesCount + 1), savedBunniesCount):
            path = constructPathForCombination(bunniesCombination)

            if countTimeForPath(path, matrix) <= time_limit:
                return sorted(list(i - 1 for i in bunniesCombination))

    return []

print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
