def isPalindrome(strNum):
    digits = [int(x) for x in strNum]
    length = len(digits)    
    endex = length//2 +1
    for i in range(0,endex):
        if(digits[i]!=digits[-i-1]):
            return False
    return True


def main():   
    #print isPalindrome("9119")
    candidates = []
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            if(isPalindrome(str(i*j))):
                candidates.append(str(i*j)+'='+str(i)+'x'+str(j))
    
    print max(candidates)
    return 1

if __name__ == '__main__':
    status = main()
    #print status