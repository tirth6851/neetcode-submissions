class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkd=set();
        for i in nums:
            if i in checkd:
                return True
            else:
                checkd.add(i)
        return False

        