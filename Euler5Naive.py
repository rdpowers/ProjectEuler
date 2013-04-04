def main():
    upto = 8
    nums = 1
    while 1:
        for y in range(1,upto+1):
            #lambda x: x//y==0,nums
            if(nums%y!=0):
                #print '{} % {} is not zero'.format(nums,y) 
                break
        else:
            print nums
            break
        nums += 1

if __name__ == '__main__':
    status = main()
    print status