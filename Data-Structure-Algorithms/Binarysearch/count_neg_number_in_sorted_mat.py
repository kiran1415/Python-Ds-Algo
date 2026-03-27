"""
1351. Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Question from leetcode

"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            count+= self.find_first_neg(grid[i])
        return count
    
    def find_first_neg(self, ar):
        n = len(ar)
        low = 0
        high = n -1
        ans = n
        while low <= high:
            mid = (high+low) // 2
            if ar[mid] <0:
                ans = mid
                high = mid - 1
            else:
                low = mid+1
        return n - ans
