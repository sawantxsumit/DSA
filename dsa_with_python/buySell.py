'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
'''

#self made solution -> could not pass all test cases in leetcode (time limit exceeded)

# def calculate_profit(prices):
#     buy,sell=0,1
#     profit=0
#     while buy!=len(prices)-1:
#         for i in range(sell,len(prices)):
#             temp=prices[i]-prices[buy]
#             if temp>profit:
#                 profit=temp
#         sell+=1
#         buy+=1
#     if profit==0:
#         return 0
#     else:
#         return profit
    
# prices=[7,1,5,3,6,4]
# prices=[7,6,4,3,1]
# res=calculate_profit(prices)
# print(res)

#method 2
#optimized by chatgpt
# def calculate_profit(prices):
#     if not prices:
#         return 0 #incase the list is empty
    
#     min_price=prices[0]
#     max_profit=0
    
#     for price in prices:
#         min_price=min(price , min_price)
#         max_profit=max(max_profit, price-min_price)
        
#     return max_profit

# prices=[7,1,5,3,6,4]
# # prices=[7,6,4,3,1]
# res=calculate_profit(prices)
# print(res)

#method 3
#by stoney codes

def calculate_profit(prices):
    l,r=0,1
    maxProfit=0
    
    while r<len(prices):
        if prices[l]<prices[r]:
            profit= prices[r]-prices[l]
            maxProfit=max(maxProfit, profit)
        else:
            l=r
        r+=1
        
    return maxProfit

prices=[7,1,5,3,6,4]
# prices=[7,6,4,3,1]
res=calculate_profit(prices)
print(res)