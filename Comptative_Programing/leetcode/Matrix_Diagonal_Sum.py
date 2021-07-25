class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat[0])
        ans = 0
        for i in range(size):
            ans = ans + mat[i][i] + mat[i][size-i-1]
            
        if(size%2 != 0):
            ans = ans - mat[int(size/2)][int(size/2)]
        return ans
        