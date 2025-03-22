class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialize balance counter to track difference
        # between left and right
        balance = 0
        # initialize count to track the number of
        # balanced substrings
        count = 0
        for char in s:
            # if character is 'L' increase balance
            if char == 'L':
                balance += 1
            # if character is 'R' decrease balance
            else:
                balance -= 1
            # when balance reaches 0, found a balanced substring
            if balance == 0:
                # this necessitates an increment in count
                count += 1
        # return the total number of balanced substrings found
        return count

# Testing
# test_cases = [
    # "RLRRLLRLRL",  # Expected output: 4
    # "RLLLLRRRLR",  # Expected output: 3
    # "LLLLRRRR",    # Expected output: 1
    # "RLRRRLLRLL",  # Expected output: 2
# ]

# Run and print results
# for i, test in enumerate(test_cases, 1):
    # print(f"Test {i}: {test} ➝ Output: {balancedStringSplit(test)}")
