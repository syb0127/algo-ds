def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        # Be careful that strings are immutable types
        temp_skill = list(skill)
        for j in range(len(s)):
            shorted = False
            if s[j] in temp_skill:
                if s[j] != temp_skill.pop(0):
                    shorted = True
                    break
        if not shorted:
            answer += 1
    return answer