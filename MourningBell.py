def length_three_cycle(adj_matrix):
    n=len(adj_matrix)
    
    def divide_and_conquer(start, end):
        if end - start <= 2:
            return 'NO'
        
        mid = (start + end) // 2

   
        for i in range(start, mid - 1):
            for j in range(mid, end - 1):
                if adj_matrix[i][j] == 1 and adj_matrix[j][i] == 1:
                    return 'YES'
                
        left_result = divide_and_conquer(start, mid)
        right_result = divide_and_conquer(mid, end)

        return 'YES' if left_result == 'YES' or right_result == 'YES' else 'NO'
    
    return divide_and_conquer(0, n)

