# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(n) == False:
            #print("Doesn't contain a bad version")
            return -1
        
        
        lastSeenBadValue = -1
        lastSeenGoodValue = -5
        change = n
        searching = True
        while(searching):
            if isBadVersion(n) == True:
                #print(str(n) + " is bad")
                lastSeenBadValue = n
                    
                #return conditions here 
                if lastSeenBadValue - 1 == lastSeenGoodValue:
                    searching = False
                    return lastSeenBadValue
                    
                #Increase/decrease by a half each time
                decrease = math.floor(change / 2)
                if decrease == 0:
                    decrease = 1
                    
                change = decrease
                n = n - decrease
                
            else:   
                #print(str(n) + " is not bad")
                lastSeenGoodValue = n
                
                #n += 1 #Works for small values of n
                #Increase/decrease by a half each time
                increase = math.floor(change / 2)
                if increase == 0:
                    increase = 1
                    
                change = increase
                n = n + increase