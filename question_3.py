def max_profit(prices):
    maximum= prices[1]-prices[0]
    for index in range(len(prices)):
        for i in range (index+1,len(prices)):
            maximum=max(prices[i]-prices[index], maximum)
    if maximum>0:       
     print (maximum) 
    else: 
     print (0) 

arrays=[]
n=int(input("Enter the number of elements in array"))
for i in range (n):
 val=int(input("Enter the prices of stocks"))
 arrays.append(val)

max_profit(arrays)
