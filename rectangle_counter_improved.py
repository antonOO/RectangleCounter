import numpy as np

rectangles_representation = [[1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 3, 0, 0, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1]]

dimension_rows = len(rectangles_representation)
dimension_cols = len(rectangles_representation[0])
max_number_of_rectangles_on_grid = dimension_rows*(dimension_rows + 1)*dimension_cols*(dimension_cols+1)/4

def find_num_incorrect_rectangles(matrix):
    mistake_count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            try:
                is_it_shared = False
                if (matrix[r][c] > 1 or matrix[r][c] == 0) and matrix[r][c+1] == 0:
                    count=(len(matrix[r][:c+1])*(len(matrix)+1))
                    mistake_count+=count
                    is_it_shared = True
                if matrix[r][c] == 0 and (matrix[r][c-1] == 0 or matrix[r][c-1] > 1):
                    count = (len(matrix[r][c:])*(len(matrix)+1))
                    if is_it_shared:
                        mistake_count+=(count - len(matrix) - 1)
                    else:
                        mistake_count+=count
            except:
                pass
    return mistake_count


print(max_number_of_rectangles_on_grid - find_num_incorrect_rectangles(rectangles_representation) - find_num_incorrect_rectangles(np.transpose(rectangles_representation)))
