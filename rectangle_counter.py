
rectangles_representation = [[1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 3, 0, 0, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1]]

test = [[1,1],
        [1,1]]

dimension_rows = len(rectangles_representation)
dimension_cols = len(rectangles_representation[0])


def check_for_full_blocks_only(submatrix, matrix, row_index, col_index, subdimension_row, subdimension_col):
    for r in range(subdimension_row):
        for c in range(subdimension_col):
            try:
                if(((matrix[row_index+r][col_index-1]) == 0 and (matrix[row_index+r][col_index]) == 0)
                    or (matrix[row_index+r][col_index-1]) > 1):
                    return False
            except:
                pass
            try:
                if(matrix[row_index+r][col_index + subdimension_col]) == 0:
                    return False
            except:
                pass
            try:
                if(((matrix[row_index-1][col_index+c]) == 0 and (matrix[row_index][col_index+c]) == 0)
                    or (matrix[row_index-1][col_index+c]) > 1):
                    return False
            except:
                pass
            try:
                if(matrix[row_index+submatrix_row][col_index+c]) == 0:
                    return False
            except:
                pass
    return True

def count_rectangles(subdimension_row, subdimension_col, matrix):
    count = 0
    for row_index in range(len(matrix)):
        if len(matrix[row_index:(row_index + subdimension_row)]) == (subdimension_row):
            for col_index in range(len(matrix[row_index])):
                if len(matrix[row_index][col_index:(col_index + subdimension_col)]) == subdimension_col:
                    submatrix = []
                    for submatrix_row in range(row_index, row_index + subdimension_row):
                        submatrix.append(matrix[submatrix_row][col_index:(col_index + subdimension_col)])
                    if check_for_full_blocks_only(submatrix, matrix, row_index, col_index, subdimension_row, subdimension_col):
                        count+=1
    return count

total_rectangles = 0
for r in range(dimension_rows):
    for c in range(dimension_cols):
        total_rectangles += count_rectangles(r+1, c+1, test)
print (total_rectangles)
