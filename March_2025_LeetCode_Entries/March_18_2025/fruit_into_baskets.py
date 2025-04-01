# pseudocode

# function total_fruit(fruits: list of integers) -> integer:
# create a hashmap (dictionary) called 'basket' to track fruit counts
# initialize basket as an empty dictionary {}
    
# initialize 'left' pointer for the start of the sliding window
# set left = 0
    
# initialize 'max_fruits' to keep track of the maximum number of fruits collected
# set max_fruits = 0

# iterate over the fruits list using a sliding window approach
# for each index 'right' and fruit in 'fruits':
        
    # add the fruit at index 'right' to the basket (or increase its count)
    # increment basket[fruit] (default to 0 if fruit is not in basket)
        
    # if more than 2 unique fruit types are in the basket, shrink the window from the left
    # while size of basket > 2:
        # decrease count of fruit at 'left' position
        # decrement basket[fruits[left]]

            # if count of that fruit becomes 0, remove it from the basket
            # if basket[fruits[left]] == 0:
                # delete basket[fruits[left]]

            # move left pointer forward (shrinking window)
            # increment left
        
        # update max_fruits with the current valid window size
        # update max_fruits = max(max_fruits, right - left + 1)

    # return the maximum number of fruits collected in any valid window
    # return max_fruits
