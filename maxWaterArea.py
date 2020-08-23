"""

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
def maxWaterArea(self, height: List[int]) -> int:
    max_area = 0
    l,r = 0,len(height)-1
    while l<=r:
        curr_max = min(height[l],height[r])*(r-l)
        max_area = max(max_area,curr_max)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_area
