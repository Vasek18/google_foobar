def solution(n):
    n = int(n)
    
    count = 0
    while n != 1:
        count += 1
        
        if n == 3:
            return count + 1
        
        if n % 2 == 0:
            n //= 2
            continue
        
        if (n // 2) % 2 == 0:
            n -= 1
            continue
        
        n += 1
            
    return count
    
print(solution('15'))
print(solution('4'))
print(solution(str(10**4 - 1)))
print(solution(str(10**308 - 1)))
print(solution(str(10**309 - 1)))
