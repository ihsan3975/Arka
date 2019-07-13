def triangle(val):
    def prime(val): 
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    return False
            return True
        else:
            return False
    
    assert 0 < val < 10
    start = 2
    for i in range(val + 1):
        for j in range(i):
            while prime(start) == False:
                start += 1
            print(start, end=" ")
            start += 1
        print()
print(triangle(5))