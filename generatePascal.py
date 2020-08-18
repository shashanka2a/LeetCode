"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


def generate(self, numRows: int) -> List[List[int]]:
  if not numRows:
      return []

  num = [[] for _ in range(numRows)]

  num[0] = [1]
  if numRows==1:
      return [num[0]]

  num[1] = [1,1]
  if numRows==2:
      return [num[0],num[1]]

  num[2] = [1,2,1] 
  for i in range(3,numRows):
      num[i].append(1)
      for j in range(i-1):
          num[i].append(num[i-1][j]+num[i-1][j+1])
      num[i].append(1)
  return num
