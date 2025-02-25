from collections import defaultdict
# handle default values from dictionary

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # initialize boomerangs count
        boomerangs_count = 0

        # iterate through each point 'i'
        for i in range(len(points)):
            # dictionary to store the frequency of distances from point 'i'
            distance_count = defaultdict(int)
            for j in range(len(points)):
                # compare point 'i' with every other point 'j'
                if i == j:
                    # skip comparison with itself
                    continue
                # Calculate the squared Euclidean distance
                d = (points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2

                # Store the frequency of this distance
                distance_count[d] += 1
            # Count the boomerangs formed by distances with frequency >= 2
            for m in distance_count.values():
                if m >= 2:
                    # Number of boomerangs from this distance
                    boomerangs_count += m * (m - 1) 
        # return the total number of boomerangs
        return boomerangs_count  
        