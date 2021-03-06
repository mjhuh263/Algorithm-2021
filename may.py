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

# ======================================================================================

# 이것이 코딩 테스트다 DFS 예제

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        print('current: ', graph[v]) 
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 - 2차원 리스트 
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

# result: 1 2 7 6 8 3 4 5

"""
1
current:  [2, 3, 8]
2
current:  [1, 7]
current:  [1, 7]
7
current:  [2, 6, 8]
current:  [2, 6, 8]
6
current:  [7]
current:  [2, 6, 8]
8
current:  [1, 7]
current:  [1, 7]
current:  [2, 3, 8]
3
current:  [1, 4, 5]
current:  [1, 4, 5]
4
current:  [3, 5]
current:  [3, 5]
5
current:  [3, 4]
current:  [3, 4]
current:  [1, 4, 5]
current:  [2, 3, 8]
"""
# ======================================================================================

# 이것이 코딩 테스트다 BFS 예제

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

# ======================================================================================

# 이것이 코딩 테스트다 DFS/BFS # 03 : 음료수 얼려 먹기

"""
구멍 뚫여 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분까리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 
-> 총 아이슼림 개수를 구하는 프로그램을 작성해야 함 

- 특정한 지점의 주변 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
- 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 다시 진행하면 연결된 모든 지점을 방문할 수 있다.
- 이와 같은 과정을 반복하며 방문하지 않은 지점의 수를 센다

ex. 
4 5
00110
000111
11111
00000

ex. 
3 3
001
010
101
"""

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위에서 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0 
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

# ======================================================================================

# 이것이 코딩 테스트다 DFS/BFS # 04 : 미로 탈출
"""
BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 참색한다. 
그러므로 (1, 1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다. 
특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.
소스코드 상에서 첫번째 시작 위치는 다시 방문할 수 있도록 되어 첫번째 시작 위치에 해당하는 값이 3ㅇ로 변경될 여지가 있다 -> 하지만 문제에서는 단순히 오른쪽 아래 위치로 이동하는 것을 요구하고 있음.

입력 예시:
56 
101010
111111
000001
111111 111111

출력:
10
"""

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기 
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치를 학인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 찾기 공간을 벗어난 경우 무시하기
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 무시하기
            if graph[nx][ny] == 0:
                continue

        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록하기
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))

# ======================================================================================

"""

[5.1 Graph Traversals - BFS & DFS]


1. visiting a vertex
2. exploration of a vertex

BFS: 1, 2, 4, 5, 7, 6, 3 - no vertex remaining to visit
-> 1, 2, 4, 5, 7, 6, 3
- explore a vertex then you go to the next vertex

DFS: 1, 2, - since you explored a new vertex you have to explore that vertex - 3 - completly explored, comeback to 2 - 6, 7 - comeback to 1 - 4, 5
-> 1, 2, 3, 6, 7, 4, 5
- explore a new vertex suspend the vertex and start its exploration

Binary Tree BFS, DFS
Level order -> BFS: 1, 2, 3, 4, 5, 6, 7
Pre-order -> DFS: 1, 2, 4, 5, 3, 6, 7

Key points:
BFS - Queue, Exploration completely done
* first in first out: After the number is completely searched it is removed
DFS - once you have reached a new vetex start exploring that vertex
* first in last outL After the number is completely searched it is removed


[geeksforgeeks Binary Search]


Binary Search Tree is a node-based binary tree data structure which has the following properties:
- the left subtree of a node contains only nodes wih keys lesser than the node's key
- the right subtree of a node contains only nodes with keys greater than the node's key
- the left and right subtree each must also be a binary search tree - there must be no duplicate nodes

The above properties of Binary Search Tree provides an ordering among keys so that the operations like search, minimum and maximum can be done fast. If there is not ordering then we may have to compare every key to search for a given key.

We will start woth a search space of 'n' nodes -> discard one of the subtrees, discard 'n/2' nodes, search space reduced to 'n/2' -> reduce to 'n/4' -> unitl search space is reduced to onl one node 


def search(root, key):
    # root is nill or key is present at root
    if root is None or root.val == key:
        return root
    # if key is greater than root's key
    if root.val < key:
        return search(root.right, key)
    # key is smaller than root's key
    return search(root.left, key)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# insert a new node with the given key
def insertkey(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insertkey(root.right, key)
        else:
            root.left = insertkey(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
r = insertkey(r, 30)
r = insertkey(r, 20)
r = insertkey(r, 40)
r = insertkey(r, 70)
r = insertkey(r, 60)
r = insertkey(r, 80)

inorder(r)

# Output:
20 
30 
40 
50 
60 
70 
80

# 시간복잡도
최악: O(h) -> O(n)

"""

# leetcode # 101 Symmetric Tree

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

ex)
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r

    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or (l.val != r.val):
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True

"""
시간제한: 30분
@OldCodingFarmer님의 solution

문제풀이 체크리스트
◼️ 시간 제한 지났음에도 문제 터치 못함
◻️ 시간 제한 후 코드 완성
◻️ 코드 미완성
◻️ 코드 완성 - 에러
◻️ 코드 완성 - 정답
"""

# ======================================================================================

"""

[Do it! 자료구조와 함께 배우는 알고리즘 입문]

내부 정렬: 정렬할 데이터를 하나의 배열에 저장할 수 있는 경우에 사용하는 알고리즘
외부 정렬: 정렬한 데이터가 많아서 하나의 배열에 저장할 수 없는 경우에 사용하는 알고리즘
** 정렬 알고리즘의 핵심은 교환, 선택, 삽입

--- 6-2 버블 정렬 ---
버블 정렬은 이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘으로 단순 교환 정렬

"""
# n개의 원소 수와 각각의 원솟값을 입력받는다. i값을 0부터 n-2까지 1을 증가시키고, 패스를 n-1번 수행.

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == "__main__":
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x =  [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]'))

    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')

"""
[이진탐색] - https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/

이진탐색트리를 순회할 때 중위순회 방식을 쓴다 - 왼쪽 서브트리-> 노드 -> 오른쪽 스브트리 순으로 순회

이진참색트리의 핵심 연산은 - 검색, 삽입, 삭제  (기타: 생성, 삭제, isEmpty, tree traverse 연산)

[637. Average of Levels in Binary Tree]

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

ex)
Input: root = [3,9,20,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

constraints)
- The number of nodes in the tree is in the range [1, 104].
- -231 <= Node.val <= 231 - 1

"""

# Leetcode # 637 Average of Levels in Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root: TreeNode):
        result = []
        level = (root,)
        while level:
            # result => sum(of the  nodes in the same level) divided with the number of nodes present on the level
            result.append(sum(node.val for node in level) / len(level))
            # level => 만일 노드에 잎새노드가 있으면 오,왼 잎새노드를 level에 넣기
            level = tuple(leaf for node in level for leaf in (node.left, node.right) if leaf)

        return result

"""
Input:
    3
   / \
  9  20
    /  \
   15   7

input: [3,9,20,null,null,15,7]

첫번째 level print - TreeNode
----------------
initial level (TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}},)

실행후 result, level print - TreeNode, tuple(TreeNode를 storage하는)
----------------
result [3.0]
level (TreeNode{val: 9, left: None, right: None}, TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}})
result [3.0, 14.5]
level (TreeNode{val: 15, left: None, right: None}, TreeNode{val: 7, left: None, right: None})
result [3.0, 14.5, 11.0]
level ()



1. start level = [3], result = []
2. sum of [3] is 3 and divide by 1, store the result 3 
3. iterate over [3], store (9, 20), itnerate over it, if they are not None store in level
4. level = [9, 20], result = [3]
5. average of level is 14.5, tierate over [9, 20] 9 got (None, None) children, 20 got (15, 7), None will not be yielded, got new level 
6. level = [15, 7], result = [3, 14.5]
7. avg is 11, new level is empty, stop while loop
8. return result = [3, 14.5, 11]

시간제한: 30분
@dan2000kr님의 solution

문제풀이 체크리스트
◻️ 시간 제한 지났음에도 문제 터치 못함
◻️ 시간 제한 후 코드 완성
◼️ 코드 미완성
◻️ 코드 완성 - 에러
◻️ 코드 완성 - 정답
"""

# BST

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if (self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if (val <= currentNode.val):
            if (currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif (val > currentNode.val):
            if (currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

# ======================================================================================

# Do it! 자료구조와 함께 배우는 알고리즘 입문 버블정렬

from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    ccnt = 0 
    scnt = 0
    n = len(a)
    
    for i in range(n - 1):
        print(f'패스 {i + 1}')
        for j in range(n - 1, i, -1):
            for m in range(0, n -1):
                print(f'{a[m]:2}' + (' 'if m != j -1 else ' +' if a[j - 1] > a[j] else ' -'), end='')

            print(f'{a[n - 1]:2}')
            ccnt += 1 
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
            for m in range(0, n-1):
                print(f'{a[m]:2}', end='')
            print(f'{a[n - 1]:2}')
        print('비교를 {ccnt}번 했습니다.')
        print('교환를 {scnt}번 했습니다.')

# 교환이 더 이상 이루어지지 않을 경우 정렬을 종료하는 코드 -> 비교 연산이 크게 줄어 실행 시간을 단축할 수 있다 

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        exchg = 0 # 패스를 시작하기 전에 0으로 초기화
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
            exchg += 1
        if exchg == 0:
            break

# 첫번째 패스의 정렬이 종료됐으면 패스를 좁혀서 비교, 교환하기 

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
        last = n -1
        for  j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
            last = j
        k = last

# 셰이커 정렬 

"""

첫번째 원소가 가장 큰 원소인 경우에는 버블 정렬이 적합하지 않다.
버블 정렬을 개선한 알고리즘이 셰이커 정렬이다 
홀수 패스에서는 가장 적은 원소를 맨 앞으로 이동시키고 짝수 패스에서는 가장 큰 원소를 맨뒤로 이동시켜 패스의 스캔 방향을 번갈아 바꾸어 본다. 

"""
from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    left = 0 # 스캔 범위의 첫 원소 인덱스
    right = len(a) - 1 # 스캔 범위의 마지막 원소 인덱스
    last = right 
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j 
        left = last 

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j

        right = last # 마지막 인덱스를 right으로 다시 넣기

# ======================================================================================

# Do it! 자료구조와 함께 배우는 알고리즘 입문 단순선택정렬

"""
1. 아직 정렬하지 않은 부분에서 값ㅇ 가장 작은 원소 a[min]을 선택한다
2. a[min]과 아직 정렬하지 않은 부분에서 맨 앞에 있는 원소를 교환합니다

for i in range(n - 1):
    min -> a애서 키값이 가장 적은 원소의 인덱스
    a[i]와 a[min]의 값을 교환합니다
"""

from typing import MutableSequence

def selection_sort(a: MutableSequence):
    n = len(a)
    for i in range(n - 1):
        min = i # 정렬할 부분에서 가장 작은 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j 
        a[i], a[min] = a[min], a[i]


# BST find

def find(self, val):
    if (self.findNode(self.root, val) is False):
        return False
    else:
        return True

def findNode(self, currentNode, val):
    if (currentNode is None):
        return False
    elif (val == currentNode.val):
        return currentNode
    elif (val < currentNode.val):
        return self.findNode(currentNode.leftChild, val)
    else:
        return self.findNode(currentNode.rightChild, val)

# ======================================================================================

# BST insert

"""

새로운 데이터는 트리의 잎새노드에 붙인다. 
삽입연산은 반드시 입새노드에서 이뤄지게 된다 

이진탐색 트리의 가장 왼쪽 잎새노드는 해당 트리의 최소값, 제일 오른쪽 잎새노드는 최대값이 된다. 
만약 위 트리에서 100을 추가하려고 한다면 제일 오른쪽 잎새노드의 오른쪽 자식노드를 만들고 여기에 붙인다. 

"""

def insert(self, val):
    if (self.root is None):
        self.setRoot(val)
    else: 
        self.insertNode(self.root, val)

def insertNode(self, currentNode, val):
    if (val <= currentNode.val):
        if (currentNode.leftChild):
            self.insertNode(currentNode.leftChild, val)
        else:
            currentNode.leftChild = Node(val)
    
    elif (val > currentNode.val):
        if (currentNode.rightChild):
            self.insertNode(currentNode.rightChild, val)
        else:
            currentNode.rightChild = Node(val)

# BST delete 

"""

case 1: 자식 노드가 없는 경우 
그냥 삭제하면 됨

case 2: 자식노드가 하나 있는 경우 
해당 노드를 지우고 해당 노드의 자식노드와 부모노드를 연결해줌
어차피 서브트리의 모든 값ㅇㄴ 부모노드보다 작다

case3: 
중위순회방식의 트리: 4, 10, 13, 16, 20, 22, 25, 28, 30, 42
삭제할 노드에 successor를 복사해놓고, 기존 successor 위치에 있던 노드를 삭제하게 되면 정렬된 순서를 유지(=이진탐색트리 속성을 만족)하면서도 결과를 얻는다

만약 successor도 predecessor도 자식 노드가 하나이거나 존재하지 안을 경우: case3로 처리 


"""

# BST 중위순회 코드

def traverse(self):
    return self.traverseNode(self.root)

def traverseNode(self, currentNode):
    result = []
    if (currentNode.leftChild is not None):
        result.extend(self.traverseNode(currentNode.leftChild))
    if (currentNode is not None):
        result.extend([currentNode.val])
    if (currentNode.rightChild is not None):
        result.extend(self.traverseNode(currentNode.rightCHild))
    return result

# ======================================================================================

# leetcode # 217 : Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# ======================================================================================

# leetcode # 387 : First Unique Character in a String