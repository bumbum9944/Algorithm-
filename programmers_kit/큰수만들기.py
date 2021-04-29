def solution(number, k):
    answer = ''
    target = set()
    for i in range(1, len(number)):
        if int(number[i]) > int(number[i-1]):
            pos = i-1
            while True:
                if int(number[pos]) < int(number[i]):
                    target.add(pos)
                else:
                    break
                if k == len(target):
                    break
                pos -= 1
                if pos < 0:
                    break
            if k == len(target):
                break
    for idx in range(len(number)):
        if idx not in target:
            answer += number[idx]
    if k != len(target) and answer[-1] < answer[-2]:
        answer = answer[:-1]
    return answer

# 문제 : 프로그래머스 고득점 kit - 그리디 - 큰 수 만들기(42883)
'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
이 중 가장 큰 숫자는 94 입니다.
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
'''
# 풀이 : 2번째 숫자부터 확인하고 앞에 숫자가 자기보다 작으면 제거한다.(큰 수만 남긴다.)
# 앞에 숫자가 자기보다 작을 경우 위치를 저장한다.
# 앞의 숫자와 크기 비교를 통해 숫자를 제거하기 때문에 마지막 위치에 있는 숫자는 제거 대상이 되지 않는다.
# 만약 제거 대상의 수가 k개에서 1개 못미칠 경우 마지막 숫자가 제거 대상인 경우다.
# 이 상황을 분기처리해준다.