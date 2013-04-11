def primeGen():
    yield 2
    atNum = 1
    while(1):
        atNum = atNum+2
        if(isPrime(atNum)):
            yield atNum

def isPrime(num):
    top = num**0.5+1
    i=3
    while i<top:
        if num%i==0:
            return 0
        i+=2
    return 1

def main():
    ctr = 0
    for j in primeGen():        
        ctr+=1
        if ctr==10001:
            print j
            break
        
        
if __name__ == '__main__':
    status = main()
    #print status