def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x
    
    # 캘 수 있는 광물의 개수
    num_min = sum * 5
    if len(minerals) > num_min: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:num_min]
        
    # 광물 조사
    cnt_min = [[0, 0, 0]for x in range(10)] # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1

    # 피로도가 높은 순서대로 광물 정렬
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))
    
    # 피로도 계산
    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: # dia 곡괭이
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: # iron 곡괭이
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: # stone 곡괭이
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
                
    return answer
    """answer = 0
    cur_pick = -1
    ind = 0
    
    while ind > len(minerals):
        print(ind)
        if ind%5 == 0:
            #if "minerals" is longer than the number of minerals that can be covered
            if sum(picks) == 0:
                return answer
            elif picks[0] > 0:
                answer += 5
                ind += 5
                picks[0] -= 1
                continue
            elif picks[1] > 0:
                cur_pick = 1
                picks[1] -=1
            else:
                cur_pick = 2
                picks[2] -= 1
        if minerals[j] == "iron":
            if cur_pick == 1:
                answer += 5
            else:
                answer += 1
        else:
            answer += 1
        ind += 1
    return answer"""