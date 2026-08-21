class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevNum = {} # val:index

        for i, n in enumerate(nums):
            comp = target - n
            if comp in prevNum:
                return [prevNum[comp], i]
            prevNum[n] = i

        return []
        
        