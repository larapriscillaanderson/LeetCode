class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # convert jewels into strings
        jewel_set = set(jewels)

        # count the number of stones that are jewels
        return sum(stone in jewel_set for stone in stones)
        