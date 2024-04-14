def length_three_cycle(adj_matrix):
    def divide_and_conquer(start, end):
        if end - start <= 2:
            return 'NO'
        
        mid = (start + end) // 2

   
        for i in range(start, mid - 1):
            for j in range(mid, end - 1):
                if adj_matrix[i][j] == 1 and adj_matrix[j][i] == 1:
                    return 'YES'
