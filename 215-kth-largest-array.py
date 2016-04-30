import heapq

def findKth(nums, k):
  heap = []

  for i in nums:
    print -i
    heapq.heappush(heap, -i)

  for j in xrange(k):
    pop = heapq.heappop(heap)
    print pop

  return -pop

print findKth([3,2,1,5,6,4], 2)
