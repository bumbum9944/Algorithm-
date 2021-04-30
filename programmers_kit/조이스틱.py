def solution(name):
    answer = 0
    target_arr = []
    target_dict = dict()
    for i in range(len(name)):
        if name[i] != 'A':
            target_arr.append(i)
            target_dict[i] = False
    now_pos = 0
    target_cnt = len(target_arr)
    while target_cnt > 0:
        minV = len(name)
        next_ch = 0
        for target in target_arr:
            if target_dict[target] == False:
                dis = min(abs(target - now_pos), len(name) - abs(target - now_pos))
                if dis < minV:
                    minV = dis
                    next_ch = target

        answer += minV
        now_pos = next_ch
        ch = name[next_ch]
        ch_change = min(ord(ch) - ord('A'), (ord('Z') - ord(ch) + 1))
        answer += ch_change
        target_dict[next_ch] = True
        target_cnt -= 1

    return answer

    # 문제 : 프로그래머스 고득점 kit - 그리디 - 조이스틱
    '''
    조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
    ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
    조이스틱을 각 방향으로 움직이면 아래와 같습니다.
        ▲ - 다음 알파벳
        ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
        ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
        ▶ - 커서를 오른쪽으로 이동
    예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
        - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
        - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
        - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
    따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
    만들고자 하는 이름 name이 매개변수로 주어질 때, 
    이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
    '''
    # 풀이 : 현재 위치의 알파벳을 변경한 후 다음 변경 알파벳의 위치를 고를 때
    # 왼쪽 오른쪽 양방향으로 이동할 수 있고 순환 방식이므로
    # 현재 위치에서 가장 가까운 위치를 선택하면서 이동하면 된다.
    # 왼쪽, 오른쪽 중 더 가까운 거리를 선택하여 알파벳을 고른다.
    # 알파벳을 변경할 때도 알파벳 순서에서 올라가거나 반대로 내려가는 것 중
    # 더 작은 횟수의 방법을 선택한다.