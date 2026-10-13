def gcdOfTwoNumbers(n1, n2):
    while n2 != 0:
        rem = n1% n2 
        n1 = n2 
        n2 = rem
    return n1
    pass