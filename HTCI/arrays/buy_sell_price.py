import sys
def find_buy_sell_stock_prices(array):
  if array == None or len(array) < 2:
    return None
  sell = array[1]
  buy = array[0]
  max_profit = sell - buy
  for i in xrange(1, len(array)):
    current_profit = array[i] - buy 
    if current_profit > max_profit:
      max_profit = current_profit
      sell = array[i]
    if buy > array[i]:
      buy = array[i]
  return sell-max_profit, sell