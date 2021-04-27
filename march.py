# leetcode # 67 : Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        result = bin(a + b)[2:]
        return result

# ======================================================================================

# 프로그래머스 : 완전탐색 모의고사 

def solution(answers):
    boss = []
    temp = []

    count_one = 0
    count_two = 0
    count_three = 0

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for x, num in enumerate(answers):
        if num == one[x % len(one)]:
            count_one += 1
        if num == two[x % len(two)]:
            count_two += 1
        if num == three[x % len(three)]:
            count_three += 1
    
    temp = [count_one, count_two, count_three]

    [boss.append(x+1) for x, num in enumerate(temp) if num == max(temp)]

    return boss


# ======================================================================================

# LeetCode # 20 : Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        lookup = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in lookup.values():
            	stack.append(p)
            elif stack and lookup[p] == stack[-1]:
            	stack.pop()
            else:
            	return False
                
        return stack == []

# ======================================================================================

# LeetCode # 704 : Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else :
                right = middle - 1
        return -1

# ======================================================================================

# LeetCode # 13 : Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50, 
            "C" : 100, 
            "D" : 500, 
            "M" : 1000
        }

        res = 0

        for i in range(len(s)):
            if i < len(s) - 1:
                if dict[s[i]] >= dict[s[i-1]]:
                    res += dict[s[i]]
                else: 
                    res -= dict[s[i]]
        return result

# ======================================================================================

# LeetCode # 70 : Climbing Stairs

class Solution:
    def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n <= 2 and n >= 0:
                return n

            f = 1
            s = 2 
            c = 0 
            
            for _ in range(2, n):
                c = f + s
                f, s  = s, c
                
            return c 

class Solution:
    
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n <= 2 and n >= 0:
            return n

        arr = [1,2]

        for i in range(2, n):
            arr.append(arr[i-1] + arr[i-2])
        
        return arr[n-1]

# ======================================================================================

# LeetCode # 448 : Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # index = abs(nums[i]) - 1
            nums[abs(nums[i]) - 1] = - abs(nums[abs(nums[i]) - 1])

        return [i+1 for i in range(len(nums)) if nums[i] > 0]

# ======================================================================================

# LeetCode # 287 : Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        s = 1
        e = len(nums)-1
        while s + 1 <= e:
            count = 0
            m = (s + e)//2
            for num in nums:
                if num <= m: 
                    count += 1        
            if count <= m:
                s = m + 1
            else:
                e = m
        return e

# ======================================================================================

# 이것이 코딩 테스트다 그리디 # 02 : 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0 
result += (count) * first
result += (m - count) * second

print(result)