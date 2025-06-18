try:
    num = int(input("Enter integer: "))
    fac = 1
    k = 0
    if num >= 0:
        while k < num:
            k+=1
            fac*=k
        print(fac)
    else:
        print('n >= 0')
except:
    print('Enter integer')