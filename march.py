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
   

print(solution([1,3,2,4,2]))


# ======================================================================================

# LeetCode # 20. : Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
            
        elif len(s) == 0:
            return False
        
        stack = []

        parameters = {")": "(", "}": "{", "]": "["}

        for string in s:
            if string in parameters:
                if stack:
                    stack_pop = stack.pop()
                
                if parameters[string] != stack_pop:
                    return False
                
            else:
                stack.append(string)

        return True