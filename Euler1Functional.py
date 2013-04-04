if __name__ == '__main__':
    nums = range(1,1000)
    print sum(filter(lambda x: x%3==0 or x%5==0,nums))
        