# sum of all divisiors is equal is number
# 6=1+2+3
data=' '
while data!='exit':
    
        n=int(input())
        def perfect_function(n):
            
            sum=0
            for i in range(1,n):
                if n%i==0:
                    sum+=i
            if sum==n:
                return True
            else:
                return False
        print(perfect_function(n))
    

