def solution(n, costs):
    answer = 0
    p = list(range(n))
    
    def find(n):
        if n != p[n]:
            p[n] = find(p[n])
        return p[n]
    
    def union(u, v):
        parent_1 = find(u)
        parent_2 = find(v)
        p[parent_2] = parent_1
        
    costs.sort(key=lambda x: x[2])
    
    for cost in costs:
        node_1 = cost[0]
        node_2 = cost[1]
        
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            answer += cost[2]
            
    return answer


    # 프로그래머스 고득점 kit 그리디 섬연결하기 문제
    # 문제 설명 :
    '''
    n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 
    최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 
    필요한 최소 비용을 return 하도록 solution을 완성하세요.
    '''

    # 최소 신장 트리(mst) 문제

    # 문제 풀이 : 
    # 크루스칼(kruskal) 알고리즘 사용

    # 다리 건설 비용을 기준으로 오름차순 정렬 후
    # 사이클을 만들지 않으면서 간선을 선택한다

    # find와 union

    # find : 노드의 부모를 찾아주는 함수
    # 연결된 노드들의 관계를 트리와 같이 계층으로 나타낼 때
    # 최상위 노드는 부모가 자기 자신이다.
    # 자기 자신인 노드가 나올 때까지 재귀호출

    # union : 두 노드를 연결해주는 함수
    # 한 노드가 다른 노드의 부모가 된다.
    # 탐색을 빠르게 하기 위해서는 rank가 낮은 트리를 
    # rank가 높은 트리에 붙이는 것이 정석이다.