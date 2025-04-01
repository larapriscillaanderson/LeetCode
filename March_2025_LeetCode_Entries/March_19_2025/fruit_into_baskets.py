class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # create a hashmap (dictionary) to keep track of the 
        # count of each fruit in the basket
        basket = {}

        # left pointer represents the start of the sliding window
        left = 0

        # variable to store the maximum number of fruits we can collect
        max_fruits = 0

        # iterate over the list using the right pointer to expand the window
        for right in range(len(fruits)):
            # get the current fruit at index right
            fruit = fruits[right]  

            # add the fruit to the basket 
            # or increase its count if it already exists
            basket[fruit] = basket.get(fruit, 0) + 1

            # if there are more than 2 types of fruit, 
            # shrink the window from the left
            while len(basket) > 2:
                # decrease the count of the fruit at the left position
                basket[fruits[left]] -= 1

                # if the count of that fruit reaches 0
                # remove it from the basket
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                # move the left pointer forward to shrink the window
                left += 1
                
            # update the maximum number of fruits collected in any valid window
            max_fruits = max(max_fruits, right - left + 1)

        # return the maximum number of fruits collected in a valid window
        return max_fruits
        