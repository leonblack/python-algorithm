def cover(board, size, tr, tc, dr, dc):
    if size <= 1:
        return
    global tile
    tile += 1
    current_tile = tile
    size //= 2
    if dr < tr + size and dc < tc + size:
        cover(board, size, tr, tc, dr, dc)
    else:
        board[tr + size - 1][tc + size - 1] = current_tile
        cover(board, size, tr, tc, tr + size - 1, tc + size - 1)
    if dr >= tr + size and dc < tc + size:
        cover(board, size, tr + size, tc, dr, dc)
    else:
        board[tr + size][tc + size - 1] = current_tile
        cover(board, size, tr + size, tc,
                   tr + size, tc + size - 1)
    if dr < tr + size and dc >= tc + size:
        cover(board, size, tr, tc + size, dr, dc)
    else:
        board[tr + size - 1][tc + size] = current_tile
        cover(board, size, tr, tc + size,
                   tr + size - 1, tc + size)
    if dr >= tr + size and dc >= tc + size:
        cover(board, size, tr + size, tc + size, dr, dc)
    else:
        board[tr + size][tc + size] = current_tile
        cover(board, size, tr + size, tc + size,
                   tr + size, tc + size)
    return board
tile =0
board = [[0]*8 for i in range(8)]
board[2][3]=-1
cover(board,8,0,0,2,3)
for row in board:
    print(("%4i"*8)%tuple(row))

