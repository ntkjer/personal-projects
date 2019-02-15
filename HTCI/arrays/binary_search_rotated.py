def binary_search_rotated(arr, key):
  # iterative solution
  # assuming all the keys are unique.
  st = 0
  end = len(arr)-1
  if st > end:
    return -1
  while st <= end:
    mid = st + (end-st)/2

    if arr[mid] == key:
      return mid

    if (arr[st] <= arr[mid] and
        key <= arr[mid] and
        key >= arr[st]):
      end = mid - 1
    elif (arr[mid] <= arr[end] and 
            key >= arr[mid] and
            key <= arr[end]):
      st = mid + 1
    elif arr[st] >= arr[mid]:
      end = mid - 1
    elif arr[end] <= arr[mid]:
      st = mid + 1

  return -1