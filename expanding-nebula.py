def solution(g):
    prevState = [[True] * (len(g[0])+1) for i in range(len(g)+1)]

    return countPrevStates(g, 0, 0, prevState, [], {})

def countPrevStates(state, y, x, prevState, history, cache):
    prevStateRowsCount = len(state) + 1
    prevStateColumnsCount = len(state[0]) + 1

    if (x == prevStateColumnsCount):
        return 1

    cacheKey=((y,x), tuple(history[-(len(state)+2):]))

    if cacheKey in cache:
        return cache[cacheKey]

    count = 0

    for valueCandidate in [True, False]:
        if (not y or not x) or cellCanHasValueOf(valueCandidate, y, x, state, prevState):
                prevState[y][x] = valueCandidate

                history.append(valueCandidate)
                count += countPrevStates(
                    state,
                    (y + 1) % prevStateRowsCount,
                    x + (y + 1) // prevStateRowsCount,
                    prevState,
                    history,
                    cache
                )
                history.pop()

    cache[cacheKey] = count

    return count

def cellCanHasValueOf(value, y, x, state, prevState):
    return ((prevState[y][x-1] + prevState[y-1][x]
            + prevState[y-1][x-1] + value)==1) == state[y-1][x-1]