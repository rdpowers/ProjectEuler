def getProduct(strNum):
    digits = [int(x) for x in strNum]
    #print digits
    product = reduce(lambda y,z:y*z,digits)
    return product

def main():
    fileobj = open("Euler8Data", "r")
    strIn = fileobj.read()
    strIn = strIn.replace('\n','').replace('\r','')
    maxProduct = 0
    while True:
        strFront = strIn[:5]        
        if not strFront:
            break
        elif strFront[-1]=='0':
            strIn=strIn[4:]
        else:
            newProduct = getProduct(strFront)
            if newProduct>maxProduct:
                maxProduct = newProduct
                       
        strIn = strIn[1:]
    print maxProduct
             
    
if __name__ == '__main__':
    status = main()
    