class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # compute the sum of the first k elements (initial window)
        # nums[:k] takes the first k elements of the array (from index 0 to k-1)
        window_sum = sum(nums[:k])
        # initialize max sum to the first window sum
        max_sum = window_sum

        # slide the window across the array, starting from index k
        # remove the leftmost element and adding the next rightmost element 
        for i in range(k, len(nums)):
            # remove the element that is sliding out (nums[i-k])
            # and add the new element coming in (nums[i])
            window_sum += nums[i] - nums[i - k]

            # update max_sum if the new window sum is larger
            max_sum = max(max_sum, window_sum)

        # compute the maximum average by dividing k
        return max_sum / float(k)
        