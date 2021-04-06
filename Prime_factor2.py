#Program on prime_factor2
import math
n=int(input())
def primeFactors(n):
    while n % 2 == 0:
        print (2),
        n = n / 2
       
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            print (i),
            n = n / i
            
    if n > 2:
        print (n)
primeFactors(n)




#Program on Prime_number_39
num=int(input())
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print('False')
else:
        print('True')