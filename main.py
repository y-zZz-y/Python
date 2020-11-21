def pow(a:float,n:int):
    """
    Быстрое возведение в степень (рекурсия)
    """
    if n==0:
        return 1
    elif n%2==1: #нечетное
        return pow(a,n-1)*a
    else: #четное
        return pow(a**2,n//2)

    #return 1 if n==0 else if n%2==1 pow(a,n-1)*a else pow(a**2,n//2)

print(pow(2,1000))