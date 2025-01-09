#So the solution that I have in mind is translate plain language into algo. 
#Going to the right is just picking the first row of the matrix.
#Goind down is to pick the last element of every row. 
#Going left is to reverse the last row of the matrix.
#Going up is select the first element of every row starting from the last row. 
#We start in the next iteration of the cycle. 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix[0])
        m=len(matrix)
        result=[]
        while matrix: #If the matrix is not empty 
        #First thing is just the print the first row aka going right
            result+=matrix.pop(0)
            if matrix and matrix[0]:
                #Now we have to go down, so that's last element of every row
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                 #now we have to go the left, which is reversing the last row 
                    result+=matrix.pop()[::-1]
            if matrix and matrix[0]: 
                #Finally we have to go up if its possible, that is, first element of the leftovers 
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result
