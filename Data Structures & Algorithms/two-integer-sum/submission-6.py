class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        n = len(nums)

        # I may need a hashmap with indices and values
        # so that I can easily find a number nums[j], such that
        # target-nums[i]=nums[j].

        # The brute force way will be to have two nested loops,
        # which will increase our time complexity to O(n^2)

        hashMap = {}

        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement],i]
            if nums[i] not in hashMap:
                hashMap[nums[i]] = []
            hashMap[nums[i]] = i

