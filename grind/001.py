class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {
            nums[0]: 0
        }
        i = 1
        while i<len(nums):
            diff = target - nums[i]
            if diff in seen:
                return [[diff], i]
            else:
                seen[nums[i]] = i
            
            i+=1
        




if __name__ == "__main__":
    s = Solution()
    s.twoSum([1, 2, 3, 4, 5], 6)