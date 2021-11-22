import time
import datetime

    class Solution:
        def game(self, guess: list[int], answer: list[int]) -> int:
            count = 0
            for i in range(3):
                if guess[i] == answer[i]:
                    count += 1
            return count
    
start_time = datetime.datetime.now()
x = Solution().game([1,2,3],[1,2,3])
end_time = datetime.datetime.now()
print(x)
print(end_time - start_time)
