def countPrimes(n):
    if n < 2 :
        return 0
    count = 1 
    for i in range (3 , n + 1 ):
        is_prime = True 
        for j in range ( 2,int(i**0.5) +1):
            if i %j == 0 :
                is_prime = False 
                break 
        if is_prime:

            count = count + 1 
    return count 