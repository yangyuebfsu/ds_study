'''
746. Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost.insert(0, 0)
        # length = len(cost)
        # def cost_to_end(i):
        #     if i >= length - 2:
        #         return cost[i]
        #     else:
        #         return cost[i]+ min(cost_to_end(i+1), cost_to_end(i+2))
        # return cost_to_end(0)
        # exceed time limit, need to save tempory results of recursion
        cost.insert(0, 0)
        length = len(cost)
        result = {}
        result[length-1] = cost[length-1]
        result[length-2] = cost[length-2]
        i = length-3
        while i >= 0:
            result[i] = cost[i] + min(result[i+1], result[i+2])
            i = i - 1
        return result[0]
