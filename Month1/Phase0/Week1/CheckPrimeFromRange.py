import math

def checkPrime(n):
    isPrime = True
    maxPrim = 0
    for i in range(2,n):
        isPrime = True
        if i==1 or i==2 or i==3:
            maxPrim = i
            print(f"{i} is prime")
        else:
            val = int(math.sqrt(i))
            #print(val)
            for j in range(2,val+1):
                if i%j == 0:
                     isPrime = False
                     break
                
            if isPrime == True:
                print(f"{i} is Prime")
            else:
                print(f"{i} is Not Prime")
                
if __name__ == "__main__":
    print("Finding Prime numbers in range of 20 number")
    checkPrime(20)



        
    