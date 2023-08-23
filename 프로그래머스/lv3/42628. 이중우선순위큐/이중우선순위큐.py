from heapq import *

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        o, num = operation.split()
        num = int(num)
        
        if o == "I":
            heappush(heap, num)
        else:
            if not heap:
                continue
            elif num == -1:
                heappop(heap)
            else:
                max_val = max(heap)
                heap.remove(max_val)
              
    if len(heap) == 0:
      return [0,0]
    else:
      return [max(heap), heappop(heap)]
