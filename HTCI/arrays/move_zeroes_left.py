def move_zeros_to_left(A):
  count = 0
  for i in range(len(A)-1, -1, -1):
    if A[i] == 0:
      del(A[i])
      count += 1
  zeroes = [0 for i in xrange(count)]
  A[:] = zeroes + A
  return A
     