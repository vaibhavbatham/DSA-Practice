class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row_total = len(matrix)
        col_total = len(matrix[0])
        total_elements = row_total * col_total
        count = 0

        ans = []

        row_start = 0
        col_start = 0
        row_end = row_total - 1 
        col_end = col_total - 1

        while (count < total_elements):

            #row_start -> col_start , col_end
            for i in range (col_start , col_end + 1):
                ans.append(matrix[row_start][i])
                count+=1
            row_start += 1

            if count == total_elements:
                break

            #col_end -> row_start , row_end
            for i in range (row_start , row_end+1):
                ans.append(matrix[i][col_end])
                count+=1
            col_end -= 1

            if count == total_elements:
                break

            # row_end -> col_end , col_start
            for i in range (col_end , col_start -1 , -1):
                ans.append(matrix[row_end][i])
                count+=1
            row_end -= 1

            if count == total_elements:
                break

            # col_start -> row_end , row_start 
            for i in range(row_end , row_start -1 , -1):
                ans.append(matrix[i][col_start])
                count +=  1
            col_start += 1

            if count== total_elements:
                break

        return ans 