try:
    print('num ∈ [0,200]!')
    num = int(input('Enter number: '))
    if 0 <= num <= 200:
        p = 0
        res = 1
        for l in range(1,num+1):
            p += 1
            res *= p
        print(res)
    else:
        print('num ∈ [0,200]!!!')
except:
    print('Enter integer')
