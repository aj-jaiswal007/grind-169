class Solution:

    def two_sum(self, nums: list[int], start: int, target: int)->set[tuple[int]]:
        end = len(nums)-1
        ans = set()
        while start<end:
            if nums[start] + nums[end] > target:
                # reduce
                end-=1
            elif nums[start] + nums[end] < target:
                # increase
                start+=1
            else:
                # answer
                ans.add((nums[start], nums[end]))
                start+=1
                end-=1
        
        return ans



    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answers = []
        N = len(nums)
        nums.sort()

        for i in range (0, N-2):
            if i>0 and nums[i]==nums[i-1]:
                continue



            a = nums[i]
            temp_ans = self.two_sum(nums=nums, start=i+1, target= 0-a)
            for ans in temp_ans:
                answers.append([a, ans[0], ans[1]])
        
        return list(answers)
    
if __name__ == "__main__":
    print(Solution().threeSum( [-1,0,1,2,-1,-4]))