#a is sorted list
def binary_search(a, key):
  #TODO: Write - Your - Code
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
 