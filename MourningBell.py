def length_three_cycle(adj_matrix):
    def divide_and_conquer(start, end):
        if end - start <= 2:
            return 'NO'
