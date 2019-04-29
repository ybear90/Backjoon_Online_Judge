'''
정보 초등학교 6학년 여학생들은 단체로 2박 3일 수학여행을 가기로 했다.
학생들이 묵을 숙소에는 방의 정원(방 안에 있는 침대 수)을 기준으로 세 종류의 방이 있으며, 같은 종류의 방들이 여러 개 있다.
정보 초등학교에서는 학생들에게 이 방들을 배정하되, 배정된 모든 방에 빈 침대가 없도록 하고자 한다.
예를 들어, 방의 종류가 5인실, 9인실, 12인실이고 6학년 여학생 전체가 113명 이라면, 
5인실 4개, 9인실 5개, 12인실 4개를 예약하면 각 방에 남는 침대 없이 배정이 가능하다.
또한 12인실은 사용하지 않고 5인실 10개와 9인실 7개만 사용하는 것도 가능하다. 
그러나 방의 종류가 3인실, 6인실, 9인실이고 6학년 여학생 전체가 112명이라면 빈 침대 없이 방을 배정하는 것은 불가능하다.
방의 정원을 나타내는 서로 다른 세 자연수와 전체 학생 수를 나타내는 자연수 하나가 주어졌을 때, 배정된 모든 방에 빈 침대가 없도록 방 배정이 가능한지를 결정하는 프로그램을 작성하시오. 단, 세 종류의 방은 모두 충분한 개수가 있다고 가정하며, 위의 예에서와 같이 세 종류의 방을 모두 활용하지 않고 한 종류 또는 두 종류의 방만 이용하여 배정하는 것도 허용한다.
'''
# v, a를 쓴 이유 : v를 통해 받은 것을 a에다가 int 형태로 저장하기 위해서
# 방법을 알았으므로(백준 도움말 참조) 이 부분은 나중에 수정할 것이다.
v = list()
a = list()
b = 0
c = 0
while True:
  # v = list() -> 선생님 첨삭 : 중복 코드이므로 삭제하는 것을 권장함.
  # v 변수는 전역범위로 설정 되어 있으므로 계속 callstack에서 살아있음.
  # 4개의 정수만 받을 동안만 반복해서 v라는 이름의 리스트에 입력 데이터를 넣는다.
  v = input().split()
  if len(v) == 4:
    break

# 받아온 수 데이터(문자형)를 정수형으로 바꿔서 a라는 리스트에 넣는다.
for i in range(len(v)):
  a.append(int(v[i]))
  
# 선생님 첨삭 : 종료 이후에 프로그램 재실행에 관한 처리가 없으므로 추가해서 채점 프로그램과
# 실제 작성한 프로그램이 어떤 경우에든지 맞춰져서 돌 수 있게끔 설정해주는게 바람직하다.
if a[0] > a[1] or a[1] > a[2] :
  # print("ERROR")
  # exit()
  while True:
  # v = list() -> 선생님 첨삭 : 중복 코드이므로 삭제하는 것을 권장함.
  # 4개의 정수만 받을 동안만 반복해서 v라는 이름의 리스트에 입력 데이터를 넣는다.
  v = input().split()
  if len(v) == 4:
    break
  

if a[3] < 1 or a[3] >300:
  print("ERROR")
  exit()

# 알고리즘 평가 : 약수와 배수의 개념을 이용해서, 방 배정이 가능한지 아닌지에 대해 판단 하도록 알고리즘을 구성한건 잘했음
# 하지만, 두개의 방, 세개의 방 등 여러개의 방을 동시에 사용하는 방법에 대한 경우의 수가 빠져있음(공약수의 개념 누락)
for i in range(a[3]):
  # a[3] -= a[2]
  # if a[3] < 0:
  #   a[3] += a[2]
  #   break
  # if a[3] == 0:
  #   print(1)
  #   break
  # 선생님 첨삭 : 위의 조건을 수학적으로 간략하게 표현하면 다음과 같다.
  if a[3] % a[2] == 0:
    print(1)

for i in range(a[3]):
  a[3] -= a[1]
  if a[3] < 0:
    a[3] += a[1]
    break
  if a[3] == 0:
    print(1)
    break

for i in range(a[3]):
  a[3] -= a[0]
  if a[3] < 0:
    a[3] += a[1]
    break
  if a[3] == 0:
    print(1)
    break

if a[3] != 0:
  print(0)
