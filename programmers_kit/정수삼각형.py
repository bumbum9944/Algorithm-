def solution(triangle):
    answer = 0
    result = [triangle[0]]
    for i in range(1, len(triangle)):
        target = triangle[i]
        temp = [0] * (i + 1)
        for j in range(i + 1):
            left = target[j]
            right = target[j]
            if j - 1 >= 0:
                left = result[i-1][j-1] + target[j]
            if j < i:
                right = result[i-1][j] + target[j]
            temp[j] = max(left, right)
        result.append(temp)
    answer = max(result[-1])
    return answer

# 문제 : 프로그래머스 고득점 kit 동적계획법 정수삼각형(43105)
'''
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 
예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
'''
# 풀이 : 현재 칸의 인덱스가 i일 때 현재 칸의 값은 이전 행의 i, i-1번째 값 중 더 큰 수를 현재 칸의 수와 합한 값이다.
# 이런 방법으로 시작부터 마지막 줄까지 값을 누적해가며 계산하고 마지막 줄에서 최대값을 구하면 된다.