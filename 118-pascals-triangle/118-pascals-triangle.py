class Solution(object):
    def generate(self, numRows):
        #idk
        #time: O(n^2)
        #space: O(n^2)
        
        #to store the set of rows in the triangle
        rows = []
        # we know the first element of every row is 1
        # this is also the "starter" row that allows us to build further rows
        rows.append([1])
        # iterate thru the number of rows specified in input (excluding the first which was added)
        for i in range(1, numRows):
            # again, we know the first elem of each row is always a 1
            row = [1]
            # get the prev row since the current row's vals are calculated from it
            prev = rows[i - 1]
            # iterate from 2nd element to current row # (non-inclusive bc prev row's length is 1 shorter)
            for m in range(1, i):
                # add the left + right elements of prev row to get the current row's val
                row.append(prev[m - 1] + prev[m])
            # we know the last elem of every row is always a 1
            row.append(1)
            # we've completed constructing the current row, so add it to the list holding all rows!
            rows.append(row)
        return rows