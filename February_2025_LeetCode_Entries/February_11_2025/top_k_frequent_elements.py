class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create a dictionary to count the frequency of each
        # element manually
        freq_map = {}
        # key = number
        # value = count of occuerences 
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        # create an empty min_heap (priority queue)
        heap = []
        # add elements to the heap based on their frequency
        for num, freq in freq_map.items():
            # push tuple (frequency and number)
            heapq.heappush(heap, (freq, num))
            # if the heap size is larger than k,
            # remove the element with the smallest frequency
            if len(heap) > k:
                # remove the least frequent element
                heapq.heappop(heap)
        # extract the numbers from the heap and return it as a list
        return [num for freq, num in heap]
        