"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
from typing import List
def countBits(self, n: int) -> List[int]:
    dp=[0]*(n+1)
    ans=[0]
    offset=1

    for i in range(1,n+1):
        if i==offset*2:
            offset=i
        dp[i]=1+dp[i-offset]
    return dp

n=5
print(countBits(None,n))
