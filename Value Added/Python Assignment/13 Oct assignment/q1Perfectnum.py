def isPerfectNumber(n):
    sum = 1 
    for i in range(2,n):


        if n % i == 0 :
            sum += i 
    return sum == n 
    pass
