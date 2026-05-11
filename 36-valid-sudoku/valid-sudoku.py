class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def is_valid(values):
            nums = []
            for v in values:
                if v != '.':
                    nums.append(v)
            return len(nums) == len(set(nums))

        
        for row in board:
            if not is_valid(row):
                return False
        
        for col in range(9):
            values = []
            for row in range(9):
                values.append(board[row][col])

            if not is_valid(values):
                return False

        for board_row in range(0, 9, 3):
            for board_col in range(0,9, 3):
                values = []
                for i in range(3):
                    for j in range(3):
                        values.append(board[board_row+i][board_col+j])
                
                if not is_valid(values):
                    return False

        return True