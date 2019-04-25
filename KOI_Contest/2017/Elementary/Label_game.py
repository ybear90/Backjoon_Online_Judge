'''
두 어린이 A, B가 딱지놀이를 한다. 딱지놀이 규칙은 다음과 같다.
두 어린이는 처음에 여러 장의 딱지를 가지고 있고, 매 라운드마다 각자 자신이 가진 딱지 중 하나를 낸다.
딱지에는 별(★), 동그라미(●), 네모(■), 세모(▲), 네 가지 모양 중 하나 이상의 모양이 표시되어 있다.
두 어린이가 낸 딱지 중 어느 쪽이 더 강력한 것인지는 다음 규칙을 따른다.

만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
예를 들어, 두 어린이 A, B가 낸 딱지가 다음 그림과 같다고 하자.
'''

# Input number of trial
N = int(input())

# scope check of N
while N < 1 or N > 1000:
    N = int(input())

# Check those who player is won.
def winner_print(A, B, num):
    # winner_a = 0
    # winner_b = 0
    if A[num] > B[num]:
        return 'A'
    elif A[num] < B[num]:
        return 'B'
    else:
        if num == 1:
            return 'D'
        return winner_print(A, B, num - 1)

# Play this game
trial = N
winner_list = []

while trial > 0:
    a_list = input().split()
    b_list = input().split()

    # Save the pattern in dictionary
    a_dic = {1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(int(a_list[0])):
        a_dic[int(a_list[i + 1])] += 1
    # print("A: ", a_dic)

    b_dic = {1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(int(b_list[0])):
        b_dic[int(b_list[i + 1])] += 1
    # print("B: ", b_dic)

    # Check which winner in this game
    winner_list.append(winner_print(a_dic, b_dic, 4))
    # print(winner_list)

    trial -= 1

# Print this result
for i in range(len(winner_list)):
    print(winner_list[i])



