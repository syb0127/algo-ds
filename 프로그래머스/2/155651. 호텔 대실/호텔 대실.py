import heapq
def solution(book_time):
    answer = 0
    heap = []
    
    def convertTime(time_str):
        hr, minute = time_str.split(":")
        return int(hr)*60+int(minute)
    
    for book in book_time:
        for i in range(len(book)):
            book[i] = convertTime(book[i])
        
    book_time.sort()

    for book in book_time:
        if len(heap) == 0:
            heapq.heappush(heap, book[1]+10)
        else:
            if book[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, book[1]+10)
    
    return len(heap)