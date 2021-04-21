def solution(tickets):
    tickets = list(map(tuple, tickets))
    tickets.sort(key=lambda x: x[1])

    def dfs(now, p, t_arr):
        if len(t_arr) == 0:
            return p

        for i in range(len(t_arr)):
            t = t_arr[i]
            if now == t[0]:
                n_t_arr = t_arr[:i] + t_arr[i+1:]
                d = t[1]
                res = dfs(d, p+[d], n_t_arr)
                if res:
                    return res
        return False

    answer = dfs("ICN", ["ICN"], tickets)

    return answer

    # 문제 설명 : 
    # 주어진 항공권을 모두 사용하여 여행경로를 짜는 문제입니다.
    # 항상 'ICN'(인천공항)에서 출발합니다.
    # 여러 항공권을 선택할 수 있는 상황이면 알파벳 순서가 앞서는 경로를 선택해야합니다.

    #문제 풀이 :
    # 항공권을 선택하는 순서에 따라서 모든 항공권을 선택하지 못할 수도 있습니다.
    # 여러 경로 중 조건에 맞는 한 가지 경로를 찾는 문제이고 DFS를 사용하여 풀 수 있다고 생각했습니다.
    # 알파벳 순서가 앞서는 경로를 찾기 위해서 티켓 배열을 정렬한 후에 DFS 탐색을 실행하였습니다.

    # 사용한 티켓은 배열에서 없애주어 중복 선택을 방지했습니다.

    # 어려웠던 점 : 
    # 재귀를 돌면서 모든 티켓을 사용할 수 없는 경우가 있는데 반환 값을 조정하여 처리하는 것이 까다로웠습니다.
    # 처음에 티켓을 삭제하는 대신 USED 집합을 만들어 사용여부를 표시했는데 같은 여행 코스가 반복되는 경우(사이클)을
    # 처리할 수 없었기 때문에 티켓을 삭제하는 방식으로 바꿔 해결할 수 있었습니다.