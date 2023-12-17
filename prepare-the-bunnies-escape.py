def getMapWithDistances(startX, startY, map):
    h = len(map)
    w = len(map[0])
    mapWithDistances = [[None for i in range(w)] for i in range(h)]
    mapWithDistances[startX][startY] = 1

    cellsToMark = [(startX, startY)]
    while cellsToMark:
        x, y = cellsToMark.pop(0)

        for direction in [[1,0], [-1,0], [0,-1], [0,1]]:
            nextCellX, nextCellY = x + direction[0], y + direction[1]

            if nextCellX < 0 or nextCellX >= h or nextCellY < 0 or nextCellY >= w:
                continue

            if mapWithDistances[nextCellX][nextCellY] is not None:
                continue

            mapWithDistances[nextCellX][nextCellY] = mapWithDistances[x][y] + 1

            if map[nextCellX][nextCellY] == 1:
                continue

            cellsToMark.append((nextCellX, nextCellY))

    return mapWithDistances

def solution(map):
    w = len(map[0])
    h = len(map)

    mapColouredFromStart = getMapWithDistances(0, 0, map)
    mapColouredFromEnd = getMapWithDistances(h - 1, w - 1, map)

    board = []

    minLength = 21 * 21
    for y in range(h):
        for x in range(w):
            if not mapColouredFromStart[y][x] or not mapColouredFromEnd[y][x]:
                continue

            minLength = min(mapColouredFromStart[y][x] + mapColouredFromEnd[y][x] - 1, minLength)

    return minLength


print(solution([
[0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]
]))

print(solution([
[0, 1, 1, 0],
[0, 0, 0, 1],
[1, 1, 0, 0],
[1, 1, 1, 0]
]))

print(solution([
[0, 1, 1, 0],
[0, 1, 0, 1],
[1, 1, 0, 0],
[1, 1, 1, 0]
]))

print(solution([
[0, 1, 1, 1],
[1, 0, 1, 1],
[1, 0, 0, 0],
[1, 1, 1, 0]
]))

print(solution([
[0, 1],
[1, 0],
]))

print(solution([
[0, 0],
[0, 0],
]))
