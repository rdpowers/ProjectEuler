def factorList(n):
    fList = [1]
    while n%2==0:
        fList.append(2)
        n/=2
    if n==1: return fList
    top = 1 + int(pow(n,0.5))
    for factor in range(3,top,2):
        while n%factor==0:
            fList.append(factor)
            n/=factor
            if n==1:
                break
        if n==1:
            break
    if n>1:
        fList.append(n)
    return fList

if __name__ == '__main__':
    print factorList(600851475143)
            