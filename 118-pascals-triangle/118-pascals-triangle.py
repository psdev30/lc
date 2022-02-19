class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = []
        rows.append([1])
        for i in range(1, numRows):
            row = [1]
            prev = rows[i - 1]
            for m in range(1, i):
                row.append(prev[m - 1] + prev[m])
            row.append(1)
            rows.append(row)
        return rows