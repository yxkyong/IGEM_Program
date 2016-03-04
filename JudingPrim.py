# IGEM_Program
#judging Prime
#python 2.7
import math
def judgingPrime(number):
    if (number==2) or (number==3):
        return True
    #因为大多数为合数，进行筛选可以大幅提高效率
    if (number % 6!=1) and (number % 6 !=5):
        return False
    for i in range(5,(int)(math.sqrt(number))):
        if(number % i==0) or (number %(i+2)==0):
            return False
    return True

if __name__ == '__main__':
    for k in range(1,10000):
        if(judgingPrime(k)):
                #python 3.4 :print(k)
                print k  
