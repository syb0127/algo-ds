def solution(plans):
    stck = []
    answer = []
    
    def convertTime(arr):
        for item in arr:
            hr, minute = item[1].split(":")
            item[1] = int(hr)*60 + int(minute)
            item[2] = int(item[2])
            
    convertTime(plans)
    plans.sort(key=lambda x: x[1])
    
    prev_time = 0
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        elapsed_time = start - prev_time
        
        while stck and elapsed_time > 0:
            if elapsed_time >= stck[-1][1]:
                answer.append(stck[-1][0])
                elapsed_time -= stck[-1][1]
                stck.pop()
            else:
                stck[-1][1] -= elapsed_time
                elapsed_time = 0
                
        prev_time = start
        stck.append([name, playtime])
        
    while stck:
        answer.append(stck[-1][0])
        stck.pop(-1)
                
    return answer