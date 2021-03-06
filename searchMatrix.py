"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def BinarySearch(arr,target):
        low,high = 0,len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if target < arr[mid]:
                high = mid-1
            elif target > arr[mid]:
                low = mid+1
            else:
                return True
        return False

    if not matrix:
        return False
    for i in range(len(matrix)):
        if(BinarySearch(matrix[i],target)):
            return True
    return False
