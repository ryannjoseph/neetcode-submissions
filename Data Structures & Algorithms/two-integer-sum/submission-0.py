# Input: Array named nums, int named targt 
# Output:Returning Indices i and k to equal a targt

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}  # value -> index

        for i, num in enumerate(nums):
            difference = target - num

            if difference in hashmap:
                return [hashmap[difference], i]

            hashmap[num] = i