"""
We have an integer array prices listing the prices of items from a shop. Items can receive a special discount based on the price of the next item on the list that is less than or equal to it (if such an item exists). In other words, the discount for prices[i] is prices[j], where j > i, prices[j] <= prices[i], and j is the smallest such index that satisfies these conditions.

The task is to calculate the final price for each item, after applying this special discount, and return these final prices in an array called answer.
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        answer = [-1] * l 
        st = []
        for i in range(l-1, -1, -1):
            while st and st[-1] > prices[i]:
                st.pop()
            if st:
                answer[i] = prices[i]-st[-1]
            st.append(prices[i])

        for i in range(l):
            if answer[i] ==  -1:
                answer[i] = prices[i]
        return answer



        