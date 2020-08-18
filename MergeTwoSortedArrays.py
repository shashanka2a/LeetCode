"""
Given two sorted arrays, we need to merge them in O((n+m)*log(n+m)) time with O(1) extra space into a sorted array, 
when n is the size of the first array, and m is the size of the second array.

Example:

Input: ar1[] = {10};
       ar2[] = {2, 3};

Output: ar1[] = {2,3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
       
Output: ar1[] = {1, 2, 3, 5, 8, 9, 10, 13, 15, 20}

"""        
       
import math

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    nums1.sort()
    nums2.sort()
    for _ in range(len(nums1)-m):
        nums1.remove(0)
    """
   
    nums1[len(nums1):] = nums2[:len(nums2)]

    #Shell Sort Modification
    
    gap = math.ceil(len(nums1)/2)

    while gap!=0:
        p1,p2 = 0,gap
        while p2 < len(nums1):
            if nums1[p2] < nums1[p1]:
                nums1[p1],nums1[p2] = nums1[p2],nums1[p1]
            p1+=1
            p2+=1
        if gap>1:
            gap = math.ceil(g/2)
        else:
            gap//=2
