def solution(n, results):
    answer = 0
    result_dict = dict()
    for i in range(1, n + 1):
        result_dict[i] = {
            'win': set(),
            'lose': set()
        }

    for result in results:
        winner = result[0]
        loser = result[1]
        result_dict[winner]['win'].add(loser)
        result_dict[loser]['lose'].add(winner)

    for i in range(1, n+1):
        for loser in list(result_dict[i]['win']):
            result_dict[loser]['lose'] = result_dict[loser]['lose'] | result_dict[i]['lose']
        for winner in list(result_dict[i]['lose']):
            result_dict[winner]['win'] = result_dict[winner]['win'] | result_dict[i]['win']

    for i in range(1, n + 1):
        total = 0
        total += len(result_dict[i]['win'])
        total += len(result_dict[i]['lose'])
        if total == n - 1:
            answer += 1

    return answer

    # 프로그래머스 고득점 kit 그래프/순위/49191

    # 문제 : 
    '''
        n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 
        권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 
        A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 
        하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
        선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
        정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.
    '''

    # 풀이 :
    # A와 B의 대결에서 A가 승리했을 경우 B가 승리한 모든 선수를 A가 이길 것을 예상할 수 있다.
    # 반대로 B는 A가 패배한 모든 상대에 마찬가지로 패배할 것임을 알 수 있다.
    # 이 원리에 따라 주어진 대진 정보에서 예상할 수 있는 모든 경기 결과를 기록하고
    # 전체 대진 결과인 인원수 - 1개의 결과가 저장된 경우 순위가 확정되었다고 볼 수 있다.