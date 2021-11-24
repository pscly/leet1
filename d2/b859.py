# 亲密字符串
# https://leetcode-cn.com/problems/buddy-strings/


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        




# class Solution:
#     def buddyStrings(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
#         if s == goal:
#             if len(set(s)) < len(s):
#                 return True
#             else:
#                 return False
#         diff = [(a,b) for a,b in zip(s, goal) if a != b]
#         return len(diff) == 2 and diff[0] == diff[1][::-1]            
        
print(Solution.buddyStrings(Solution, "ab", "ba"))
print(Solution.buddyStrings(Solution, "aa", "aa"), 't')
print(Solution.buddyStrings(Solution, "ab", "ab"), 'f')

