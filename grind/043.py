
"""https://leetcode.com/problems/insert-interval/description/"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        N = len(intervals)

        # First half
        while i<N and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1

        min_range = newInterval[0]
        max_range = newInterval[1]
        # Maybe or not overlapping
        while i<N and intervals[i][0] <= newInterval[1]:
            # overlapping interval
            min_range = min(intervals[i][0], min_range)
            max_range = max(intervals[i][1], max_range)

            i += 1
        
        res.append([min_range, max_range])

        # Insert rest as is
        while i<N:
            res.append(intervals[i])
            i+=1

        
        return res


if __name__ == "__main__":
    s = Solution()
    resp = s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    print(resp)