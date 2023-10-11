def solution(keymap, targets):
    answer = []
    hashmap = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            character = keymap[i][j]
            if character not in hashmap:
                hashmap[character] = j+1
            else:
                hashmap[character] = min(hashmap[character], j+1)
    for t in targets:
        cnt = 0
        for ch in t:
            if ch not in hashmap:
                cnt = -1
                break
            else:
                cnt += hashmap[ch]
        answer.append(cnt)
    return answer