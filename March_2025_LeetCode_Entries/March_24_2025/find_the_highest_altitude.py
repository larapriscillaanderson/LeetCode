class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # initialize altitude to start at 0
        altitude = 0
        # keep a max altitude tracker variable for the highest point
        max_altitude = 0
        for change in gain:
            # update altitude
            altitude += change
            # always keep track of the maximum to find highest point
            max_altitude = max(max_altitude, altitude)
        # return highest altitude
        return max_altitude

# Testing
# gain = [3, -2, 5, -1]
# print(largestAltitude(gain))  
# Output should be 6
