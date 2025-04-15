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
        
        return HappyNumbers(s)
            
    return 0 
    
    



n = 19

print(HappyNumbers(n))