# 이것이 코딩 테스트다 구현 # 02 : 시각

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# ======================================================================================

# 이것이 코딩 테스트다 구현 # 03 : 게임 개발
# 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적

"""
캐릭터 움직임 메뉴얼 
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재 -> 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진. 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단게로 돌아감
3. 만약 4방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우 바라보는 방향을 유지한채 한 칸 뒤로 가고 1단계로 돌아감. 단 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

d의 방향값:
0 - 북쪽
1 - 동쪽
2 - 남쪽
3 - 서쪽

3 3   - n, m 
1 1 0 - 캐릭터의 x,y,방향
1 1 1 - 여기서 부터는 전체 맵 정보
1 0 0 
1 1 0
"""

n,m = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장힉 위한 0으로 이루어진 맵 생성

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리를 위한 마킹

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1 
    if direction == -1:
        direction = 3

count = 1 
turn_time = 0
while True:
    turn_left() # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0: # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동함
        d[nx][ny] = 1
        x = nx 
        y = ny 
        count += 1 
        turn_time = 0 
        continue
    else:
        turn_time += 1 # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우

    if turn_time == 4: # 네 방향 모두 갈 수 없는 경우 -> 뒤로 갈 수 있다면 이동 (x,y)값으로 캐릭터 위치 재설정
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx 
            y = ny 
        else: # 뒤가 바다로 막혀 있는 경우 멈춤
            break 
        turn_time = 0

print(count)

# ======================================================================================

# 이것이 코딩 테스트다 구현 # 02 : 왕실의 나이트

"""
8 * 8 좌표 평면
- L자 이동
- 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
- 수직으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
행: 1~8
열: a~h

나이트의 현재 위치가 주어지면 현재 위치에서 이동 경로를 더한 다음, 8 * 8 좌표 평면에 있는지 확인하면 됨 -> 반복문 처리

ex. a1
"""
'''
ord() 아스키 코드 변환 함수
'''

input_data = input() 
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1), 
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인하기
result = 0 
for step in steps:
    # 이동하고자 하는 위치 확인하기 - row, column
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동할 수 있다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)