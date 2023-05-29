def solution(park, routes): 
    answer = [0,0] 
    for i in range(len(park)): 
        for j in range(len(park[0])): 
            if park[i][j] == 'S': 
                answer = [i, j] 

    move = { 'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0] }
    
    for route in routes:
        op, num = route.split(' ') 
        num = int(num) 
        nx, ny = answer  

        step = 0 
        while step < num: 
            nx += move[op][0] 
            ny += move[op][1]

            if nx < 0 or len(park) <= nx or ny < 0 or len(park[0]) <= ny or park[nx][ny] == 'X': #x y축이 경계를 벗어났는지 확인, X(장애물)을 만났는지 확인
                break 
            step += 1 #

        if step == num: 
            answer = [nx, ny] 

    return answer