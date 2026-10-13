def Lcm(n1, n2):
    a =n1
    b =n2
    while b != 0:
        rem = a % b
        a =  b
        b = rem
    return (n1*n2)//a
    
    pass