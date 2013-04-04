def main():
    rng = range(1,100+1)
    sumSquares = sum(map(lambda x: x**2,rng))
    squaresSum = reduce(lambda y,z: y+z,rng)**2 
#    print sumSquares
#    print squaresSum
    print squaresSum-sumSquares
    
if __name__ == '__main__':
    status = main()