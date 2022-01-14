def solution(rows, columns, queries):
    answer = []
    board = []
    for i in range(columns):
        for j in range(rows):
            board.append(i*rows + j + 1)
    
    # 쿼리가 1개일때 최소만 찾게 만듬.
    if len(queries) == 1:
        x1, y1, x2, y2 = queries[0]
        answer.append(board[(x1-1)*columns + y1-1])
        
    else:
        for query in queries:
            x1, y1, x2, y2 = query
            min = 100000
            
            # row방향 증가
            
            a = board[(x1-1)*columns + y1-1]
            for i in range(y1,y2):
                if a < min:
                    min = a
                b = board[(x1-1)*columns + i]
                board[(x1-1)*columns + i] = a
                a = b
            
            # col방향 증가
            for i in range(x1,x2):
                if a < min:
                    min = a
                b = board[i*columns + y2-1]
                board[i*columns + y2-1] = a
                a = b
                    
            # row방향 감소
            for i in reversed(range(y1-1,y2-1)):
                if a < min:
                    min = a
                b = board[(x2-1)*columns + i]
                board[(x2-1)*columns + i] = a
                a = b
                    
            # col방향 감소
            for i in reversed(range(x1-1,x2-1)):
                if a < min:
                    min = a
                b = board[i*columns + y1-1]
                board[i*columns + y1-1] = a
                a = b
                    
            answer.append(min)
                    
    return answer
