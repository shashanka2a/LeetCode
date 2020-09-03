"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
"""


def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals)==1 or len(intervals)==0:
        return 0
    intervals = sorted(intervals, key=lambda x: x[1])
    curr = intervals[0]
    ans = 1
    for interval in intervals:
        if curr[1] <= interval[0]:
            curr = interval
            ans += 1
    return len(intervals) - ans
