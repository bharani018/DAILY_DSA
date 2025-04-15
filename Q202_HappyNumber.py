def HappyNumbers(n):
    
    s = 0
    c = 0
    while s!=1:
        c+=1
        temp = n
        temp %= 10
        print(temp)
        s += (temp * temp)
        n //= 10
        print(s)
        print(n)
        
        if(s==1):
            return True
        if(n==0):
            return False
        return HappyNumbers(s)
    
    



n = 2

print(HappyNumbers(n))