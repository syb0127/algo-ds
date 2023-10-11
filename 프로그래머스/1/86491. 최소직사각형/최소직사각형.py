def solution(sizes):
    answer = 0
    width = 1
    height = 1
    for size in sizes:
        w, h = size
        width = max(width, w, h)
        height = max(height, min(w, h))
    return width*height

    """flattened_sizes = sum(sizes, [])
    flattened_sizes.sort()
    ind = -1+int((len(flattened_sizes)/2))*-1
    return flattened_sizes[-1]*flattened_sizes[ind]"""