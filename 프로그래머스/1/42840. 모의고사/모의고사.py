def solution(answers):
    answer = []
    three_scores = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            three_scores[0] += 1
        if answers[i] == second[i%8]:
            three_scores[1] += 1
        if answers[i] == third[i%10]:
            three_scores[2] += 1
    maximum_score = max(three_scores)
    for j in range(3):
        if three_scores[j] == maximum_score:
            answer.append(j+1)
    return answer