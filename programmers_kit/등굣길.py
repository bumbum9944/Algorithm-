def solution(m, n, puddles):
    field = [[0] * m for _ in range(n)]
    
    field[0][0] = 1

    for puddle in puddles:
        field[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0 or field[i][j] == -1:
                continue
            top = 0
            left = 0
            if i-1 >= 0 and field[i - 1][j] != -1:
                top = field[i - 1][j]
            if j-1 >= 0 and field[i][j - 1] != -1:
                left = field[i][j - 1]
            field[i][j] = top + left
    answer = field[-1][-1] % 1000000007
    return answer

# 문제 : 프로그래머스 고득점 kit - 동적계획법 - 등굣길(42898)
'''
가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 
즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 
1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
'''
# 풀이 : 현재 칸에서 좌, 상 두 칸의 경로 수를 더해 현재 칸에 저장한다.