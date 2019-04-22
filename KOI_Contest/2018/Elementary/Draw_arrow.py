'''
직선 위에 위치를 나타내는 0, 1, 2, ...와 같은 음수가 아닌 정수들이 일정한 간격으로 오른쪽 방향으로 놓여 있다.
이러한 위치들 중 N개의 위치에 하나씩 점들이 주어진다(<그림 1>). 주어진 점들의 위치는 모두 다르다. 
두 점 사이의 거리는 두 점의 위치를 나타내는 수들의 차이이다. 
<그림 1>에서는 4개의 점이 주어지고 점 a와 b의 거리는 3이다.
각 점은 N개의 색깔 중 하나를 가진다. 편의상, 색깔은 1부터 N까지의 수로 표시한다.
각 점 p에 대해서, p에서 시작하는 직선 화살표를 이용해서 다른 점 q에 연결하려고 한다. 
여기서, 점 q는 p와 같은 색깔의 점들 중 p와 거리가 가장 가까운 점이어야 한다. 
만약 가장 가까운 점이 두 개 이상이면 아무거나 하나를 선택한다.
모든 점에 대해서 같은 색깔을 가진 다른 점이 항상 존재한다. 
따라서 각 점 p에서 시작하여 위 조건을 만족하는 q로 가는 하나의 화살표를 항상 그릴 수 있다.
예를 들어, 점들을 순서쌍 (위치, 색깔) 로 표시할 때, 
a = (0,1), b = (1, 2), c = (3, 1), d = (4, 2), e = (5, 1)라고 하자. 
아래 <그림 2>에서 이 점들을 표시한다. 여기서 흰색은 1, 검은색은 2에 해당된다.

위의 조건으로 화살표를 그리면, 아래 <그림 3>과 같이 점 a의 화살표는 c로 연결된다. 
점 b와 d의 화살표는 각각 d와 b로 연결된다. 
또한 점 c와 e의 화살표는 각각 e와 c로 연결된다. 
따라서 모든 화살표들의 길이 합은 3 + 3 + 2 + 3 + 2 = 13이다.
'''
N = int(input())
if N < 2 or N > 5000:
    N = int(input())

trial = N
dot_list = list()

# Input the arrow dot numbers.
while trial > 0:
    x, y = input().split()
    coordinate = (int(x), int(y))
    dot_list.append(coordinate)
    trial -= 1
    # x, y condition
    if (coordinate[0] < 0 or coordinate[0] > 10**5) \
        or (coordinate[1] < 1 or coordinate[1] > N):
        dot_list.remove(coordinate)
        trial += 1

# Calculate length of arrow.
length = 0
for i in range(len(dot_list)):
    one_length = 100001
    for j in range(len(dot_list)):
        if (dot_list[i][1] == dot_list[j][1]) and (i != j):
            if one_length > abs(dot_list[i][0] - dot_list[j][0]):
                one_length = abs(dot_list[i][0] - dot_list[j][0])
    length += one_length

# Output the result.
print(length)