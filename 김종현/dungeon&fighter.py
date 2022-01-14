import itertools

def solution(k, dungeons):
    answer = -1
    test = list(itertools.permutations(dungeons))
    depth = 0
    m = 0
    origin = k
    for df_li in test:
        for df in df_li:
            limit, minus = df
            if origin >= limit:
                depth += 1
                origin -= minus
        if m < depth:
            m = depth
        origin = k
        depth = 0
        
    return m
