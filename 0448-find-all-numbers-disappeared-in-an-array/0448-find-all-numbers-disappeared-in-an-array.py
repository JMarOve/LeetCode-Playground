class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        aux=set(nums)
        return [i for i in range(1,(n+1)) if i not in aux]