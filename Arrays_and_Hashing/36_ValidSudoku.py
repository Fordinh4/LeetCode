def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # STEP 1: CATEGORIZE THE DATA
    row_big_list = []
    column_big_list = []
    cell_big_list = [[] for i in range(1, 10)] # For each cells
    temp_row = 0

    for row in range(len(board)):
        row_list = []
        column_list = []
        temp_col = 0
        # Condition for the cell loop to run
        if row % 3 == 0 and row != 0:
            temp_row += 3   
            
        for column in range(len(board[0])):
            # For the big row list
            try:
                row_list.append(int(board[row][column])) 
            except:
                row_list.append(0)
            
            # For the big column list
            try:
                column_list.append(int(board[column][row]))
            except:
                column_list.append(0)

            # For the big cell list
            try:
                if column % 3 == 0 and column != 0:
                    temp_col += 1
                cell_big_list[temp_row + temp_col].append(int(board[row][column]))
            except:
                cell_big_list[temp_row + temp_col].append(0)

        row_big_list.append(row_list)
        column_big_list.append(column_list)

    # STEP 2: CHECK IF THE SUDOKU BOARD IS VALID OR NOT
    
    temp_lists = [row_big_list, column_big_list, cell_big_list]
    digits_list = [i for i in range(1, 10)]

    for lists in temp_lists:
        for each_big_list in lists:
            unchecked_digits = digits_list[::]
            for number in each_big_list:
                try: 
                    if number != 0:
                        unchecked_digits.remove(number)
                except:
                    return False
    return True


# THIS IS THE COOL SOLUTION THAT I FOUND USING SET BECAUSE WE CHECK FOR UNREPEATED NUMBER SO THIS WOULD WORK SO WELL. AND THE ROWS[X] THINGY DON'T HAVE TO ADD DUPLICATE VALUE OVER TIME.
# def isValidSudoku1(board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         rows = [set() for x in range(9)]
#         columns = [set() for x in range(9)]
#         squares = [[set() for x in range(3)] for y in range(3)]
        
#         for x in range(9):
#             for y in range(9):
#                 cell_value = board[x][y]
#                 if cell_value == ".":
#                     continue
#                 if cell_value in rows[x] or cell_value in columns[y] or cell_value in squares [x//3][y//3]:
#                     return False

#                 rows[x].add(cell_value)
#                 columns[y].add(cell_value)
#                 squares[x//3][y//3].add(cell_value)
        
#         return True



board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

check = isValidSudoku(board)
print(check)