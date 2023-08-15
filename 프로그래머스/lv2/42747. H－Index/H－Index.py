def solution(citations):
    citations.sort(reverse = True)
    final_ans = 0 
    
    for ind, paper in enumerate(citations):
        if ind >= paper:
            return ind
    return len(citations)