def solution(priorities, location):
    sorted_priorities = sorted(priorities, reverse=True)
    queue = []
    for i in range(len(priorities)):
        temp = [priorities[i], False] # 우선순위, 요청 여부
        if i == location:
            temp[1] = True
        queue.append(temp)
    order = 1
    while queue:
        now_paper = queue.pop(0)
        if now_paper[0] < sorted_priorities[0]:
            queue.append(now_paper)
        else:
            if now_paper[1] == True:
                return order
            else:
                order += 1
                sorted_priorities.pop(0)
            
    return order


# 프로그래머스 고득점 kit 스택/큐 42587(프린터)


# 문제설명 :
# 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 
# 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 
# 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 
# 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 
# priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 
# 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.


# 문제풀이 :
# 주어진 문서들의 우선순위 정보를 내림차순으로 정렬하여 현재 처리해야할 문서의 우선순위를 정한다.
# queue를 이용해서 입력된 순서대로 확인한다.
# 현재 문서의 우선순위가 정렬된 우선순위의 첫번째 값보다 작은 경우 문제의 조건에 따라 가장 뒤 순서로 보낸다.
# 정렬된 우선순위의 첫번째 값과 같거나 크다면 현재 문서를 인쇄하고 정렬된 우선순위의 첫번째 값을 삭제한다.(최우선 값 갱신)