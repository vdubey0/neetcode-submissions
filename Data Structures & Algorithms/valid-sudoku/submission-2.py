class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_set = set()
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])
                    if int(board[i][j]) > 9 or int(board[i][j]) < 1:
                        return False
        
        for i in range(len(board[0])):
            col = [board[j][i] for j in range(len(board))]
            col_set = set()
            for num in col:
                if num != '.':
                    if num in col_set:
                        return False
                    else:
                        col_set.add(num)
        

        def coord_to_group(i, j):
            if 0 <= i < 3 and 0 <= j < 3:
                return 0
            elif 0 <= i < 3 and 3 <= j < 6:
                return 1
            elif 0 <= i < 3 and 6 <= j < 9:
                return 2

            if 3 <= i < 6 and 0 <= j < 3:
                return 3
            elif 3 <= i < 6 and 3 <= j < 6:
                return 4
            elif 3 <= i < 6 and 6 <= j < 9:
                return 5

            if 6 <= i < 9 and 0 <= j < 3:
                return 6
            elif 6 <= i < 9 and 3 <= j < 6:
                return 7
            elif 6 <= i < 9 and 6 <= j < 9:
                return 8
        
        group_sets = [set() for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    group = coord_to_group(i, j)
                    print(group_sets)

                    if board[i][j] in group_sets[group]:
                        return False
                    else:
                        group_sets[group].add(board[i][j])
        
        return True

        

                

        