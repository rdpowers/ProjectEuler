#getProduct takes a list of integers and multiplies them all together
def getProduct(digitsIn):
    product = reduce(lambda y,z:y*z,digitsIn)
    return product

#slices a list at a given spot
#should be able to do a generator sliding window to achieve this
def groupSets(listIn,step,fromIndex):
    return listIn[fromIndex:fromIndex+step]

def main():
    fileobj = open("Euler8Data", "r")
    strIn = fileobj.read()
    strIn = strIn.replace('\n','').replace('\r','')    
    digits = [int(x) for x in strIn]

    generatedSets = [groupSets(digits,5,i) for i in range(len(digits))]
    print generatedSets
    print max(map(getProduct,generatedSets))                
    
if __name__ == '__main__':
    status = main()
