N = int(input())
answer = 0
cars = []
front_dict = dict()
for i in range(N):
    car = input()
    front_dict[car] = cars[:]
    cars.append(car)
    

exit_cars = []
for i in range(N):
    car = input()
    exit_cars.append(car)

for i in range(N):
    car = exit_cars[i]
    back_arr = exit_cars[:i:-1]
    for bc in back_arr:
        if bc in front_dict[car]:
            answer += 1
            break

print(answer)

# 문제 : 백준 - 추월(2002)
'''
소문난 명콤비 경찰 대근이와 영식이가 추월하는 차량을 잡기 위해 한 터널에 투입되었다. 
대근이는 터널의 입구에, 영식이는 터널의 출구에 각각 잠복하고, 대근이는 차가 터널에 들어가는 순서대로, 
영식이는 차가 터널에서 나오는 순서대로 각각 차량 번호를 적어 두었다.

N개의 차량이 지나간 후, 대근이와 영식이는 자신들이 적어 둔 차량 번호의 목록을 보고, 
터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차들이 몇 대 있다는 것을 알게 되었다. 
대근이와 영식이를 도와 이를 구하는 프로그램을 작성해 보자.
'''

# 풀이 : 처음에 기존 순위에서 나왔을 때 순위가 더 앞선 차들의 수를 세어 풀었는데 오답이었다.
# 이유는 순서가 그대로 유지되거나 밀리더라도 추월한 차량인 경우가 있어서다.

# 고친 풀이 : 
# 진입하는 시점에서 자신보다 앞선 차량이 나왔을 때 뒤쪽에 있는지 여부를 체크하였다.