class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #We order first the nums list
        #We use the hashmap
        '''
        So we have orderered the num list, something like [1,2,2,3,8]
        The construction of the hashmap is 
        Step 1
        if num[i] is not in the hashmap, we record as key n[i] and as value the index i 
        {1:0}
        {"1":0,"2":1,"3":3,"8":4}
        Finally we return the value of the hash_map in the order defined by nums
        '''
        temp=sorted(nums)
        hash_map={}
        for i, num in enumerate(temp):
            if num not in hash_map:
                hash_map[num] =i
        return [hash_map[num] for num in nums]