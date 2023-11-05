'''    
Hope it will help you to understand :
    
    n = 0;     null   
    
    count[0] = 1
    
    
    n = 1;      1       
    
    count[1] = 1 
    
    
    n = 2;    1__       			 __2     
    		      \					/                 
    		     count[1]	   	count[1]	
    
    count[2] = 1 + 1 = 2
    
    
    
    n = 3;    1__				      __2__	                   __3
    		      \		            /       \			      /		
    		  count[2]		  count[1]    count[1]		count[2]
    
    count[3] = 2 + 1 + 2  = 5
    
    
    
    n = 4;    1__  					__2__					   ___3___                  
    		      \				 /        \					  /		  \			
    		  count[3]		 count[1]    count[2]		  count[2]   count[1]
    
                 __4				
               /
           count[3]   
    
    count[4] = 5 + 2 + 2 + 5 = 14     
    

And  so on...
'''
import math
class Solution(object):
# DP
    def numTrees1(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]

    # Catalan Number  (2n)!/((n+1)!*n!)  卡特兰数
    def numTrees(self, n):
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
        