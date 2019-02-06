#a is sorted list
def binary_search(a, key):
  #Run in O(log n) but has memory complexity of O(log n)
  return binary_search_helper(a, key, 0, len(a)-1)


def binary_search_helper(a, key, low, high):
  if low > high:
    return -1
  mid = low + ((high - low) // 2)
  if a[mid] == key: return mid
  elif a[mid] > key:
    return binary_search_helper(a, key, low, mid - 1)
  else:
    return binary_search_helper(a, key, mid + 1, high)
 
 def binary_search_iterative(a, key):
  low = 0
  high = len(a) - 1
  while low < high:
    mid = low + ((high - low) // 2)
    if a[mid] == key: 
      return mid
    elif key < a[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return -1
