def fib(nth):
    if nth == 0:        
        return 0
    elif nth == 1:
        return 1
    else:
        return fib(nth-1) + fib(nth-2)

def fibupto(target):
    counter = -1
    nSub0, nSub1 = 0, 1
    while nSub0 < target:
        #print nSub0
        nSub0, nSub1 = nSub1, nSub1+nSub0
        counter = counter+1
    return counter

if __name__ == '__main__':
    a = fibupto(4000000)
    q = 0
    b = 0
    for i in range(0,a+1):
        q = fib(i)
        
        if(q%2==0):
            b = b+q
            
    print b