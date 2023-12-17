def convertNumberToNBase(n, b):
    if b == 10:
        return str(n)

    n = int(n)

    if n == 0:
        return [0]

    digits = []

    while n:
        digits.append(str(n % b))
        n //= b

    return ''.join(digits[::-1])

def convertStringNumberToTenBased(n, b):
    answer = 0

    if b == 10:
        return int(n)

    for i, x in enumerate(list(n[::-1])):
        answer += int(x) * (b ** i)

    return answer

def getSortedNumbers(n, b):
    s = sorted(n)

    return ''.join(s[::-1]), ''.join(s)

def formatID(z, b, length):
    z = convertNumberToNBase(z, b)

    return (length - len(z)) * '0' + z


def countLoop(n, b, index, cache):
    if len(n) < 2:
        return 1

    index += 1

    x, y = getSortedNumbers(n, b)
    diff = convertStringNumberToTenBased(x, b) - convertStringNumberToTenBased(y, b)
    if (diff == 0):
        return 1

    n = formatID(diff, b, len(n))

    # print(x, y, diff, n, b)

    if n in cache:
        return index - cache[n]

    cache[n] = index

    return countLoop(n, b, index, cache)

def solution(n, b):
    return countLoop(n, b, 0, dict())

# print(solution('210022', 3))
# print(solution('1211', 10))
# print(solution('12', 10))
# print(solution('101', 2))
print(solution('11', 10))
