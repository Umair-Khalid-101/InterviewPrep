# TWO POINTER

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices = [7,1,5,3,6,9]

def maxProfit(prices):
  left, right = 0,1 # Left=Buy Right=Sell
  maxProfit = 0
  
  while right < len(prices):
    # PROFITABLE ?
    if prices[left] < prices[right]:
      profit = prices[right] - prices[left]
      maxProfit = max(maxProfit,profit)
    else:
      left = right
    right += 1
    
  return maxProfit

result = maxProfit(prices)
print("RESULT:",result)