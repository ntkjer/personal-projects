
def find_low_index(arr,key):
  low = 0
  high = len(arr) - 1
  mid = int(high/2)
  while (low <= high):
    mid_elem = arr[mid]
    if key >= mid_elem: low = mid + 1
    else: high = mid - 1
    mid = low + ((high-low) // 2)
  if low < len(arr) and arr[low] == key: return low
  return -1


def find_high_index(arr,key):
  low = 0 
  high = len(arr) - 1
  mid = int(high/2)
  while (low <= high):
    mid_elem = arr[mid]
    if key >= mid_elem: low = mid + 1
    else: high = mid - 1
    mid = low + ((high-low) // 2)
  if high < len(arr) and arr[high] == key: return high
  return -1
