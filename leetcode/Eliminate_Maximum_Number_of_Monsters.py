class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        count = 0
        for i in range(len(dist)):
            if i==0:
                count = count+1
            else:
                if dist[i] - speed[i] * i <=0:
                    return count
                else:
                    count = count+1
        return count
                