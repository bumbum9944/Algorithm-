def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    word_len = len(begin)
    queue = [begin]
    visited = {begin: 0}
    while queue:
        start = queue.pop(0)
        temp = []
        for word in words:
            if word in visited:
                continue
            diff_cnt = 0
            for i in range(word_len):
                if start[i] != word[i]:
                    diff_cnt += 1
            if diff_cnt == 1:
                if word == target:
                    return visited[start] + 1
                queue.append(word)
                visited[word] = visited[start] + 1
            else:
                temp.append(word)
        words = temp
        

# 문제 : 프로그래머스 고득점 kit - 깊이/너비 우선 탐색 - 단어 변환(43163)
'''
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.

예를 들어 begin이 "hit", target가 "cog", words가 
["hot","dot","dog","lot","log","cog"]라면 
"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
'''

# 풀이 :
# 단어 집합에 target 단어가 없는 경우 바로 0을 return 한다.
# 한 번에 한 개의 알파벳만 바꿀 수 있으므로 현재 단어와 다른 글자가 1개인 단어들만 바꿀 수 있다.
# 한 글자씩 바꿔가면서 target 단어를 찾으므로 이는 bfs를 이용한 최단 거리 문제와 유사하다.