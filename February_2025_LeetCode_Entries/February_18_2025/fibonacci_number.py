class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case setup
        if n == 0:
            return 0
        if n == 1:
            return 1
        # initialize the first two numbers of the fibonacci sequence
        fib_series = [0, 1]
        for index in range(2, n + 1):
            # start the loop from index 2 onwards
            next_number = fib_series[index - 1] + fib_series[index - 2]
            # append the next number to the series
            fib_series.append(next_number)
        return fib_series[n]
        