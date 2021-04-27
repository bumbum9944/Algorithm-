def solution(n, edge):
    answer = 0
    n_arr = [[] for _ in range(n+1)]
    for e in edge:
        n_arr[e[0]].append(e[1])
        n_arr[e[1]].append(e[0])
        
    queue = [1]
    visited = [0] * (n+1)
    visited[1] = 1
    
    maxV = 0
    maxN_cnt = 0
    while queue:
        node = queue.pop(0)
        for e in n_arr[node]:
            if visited[e] == 0:
                n_visited = visited[node] + 1
                if n_visited > maxV:
                    maxV = n_visited
                    maxN_cnt = 1
                elif n_visited == maxV:
                    maxN_cnt += 1
                queue.append(e)
                visited[e] = n_visited
    answer = maxN_cnt
    return answer

    # 문제 : 프로그래머스 고득점 kit 그래프/가장 먼 노드/49189
    '''
        n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 
        1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 
        간선의 개수가 가장 많은 노드들을 의미합니다.

        노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
        1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
    '''

    # 풀이 : 
    # 각 간선의 가중치가 1이므로 bfs를 사용하여 시작점에서 거리를 구할 수 있다.
    # 시작점에서의 거리를 확인하면서 최대 값을 바꿔준다.
    # 최대 거리와 같은 노드의 경우 count해주고 최대 거리가 갱신되면 count를 1로 초기화한다.