def checkmate(board_str):
    try:
        board = [list(row) for row in board_str.strip().splitlines()]
        size = len(board)

        if any(len(row) != size for row in board):
            print("Error")
            return

        directions = {
            'R': [(-1, 0), (1, 0), (0, -1), (0, 1)], #rook
            'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],#bishop
            'Q': [(-1, 0), (1, 0), (0, -1), (0, 1), #queen
                  (-1, -1), (-1, 1), (1, -1), (1, 1)],
        }

        king_pos = None
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos:
                break

        if not king_pos:
            print("Error")
            return

        for x in range(size):
            for y in range(size):
                piece = board[x][y]

                if piece in directions:
                    for dx, dy in directions[piece]:
                        i, j = x, y
                        while True:
                            i += dx
                            j += dy
                            if not (0 <= i < size and 0 <= j < size):
                                break
                            if board[i][j] == 'K':
                                print("Success")
                                return
                            if board[i][j] != '.':
                                break

                elif piece == 'P':
                    for dx, dy in [(1, -1), (1, 1)]:  # Pawn
                        i, j = x + dx, y + dy
                        if 0 <= i < size and 0 <= j < size:
                            if board[i][j] == 'K':
                                print("Success")
                                return

        print("Fail")
    except Exception:
        print("Error")
