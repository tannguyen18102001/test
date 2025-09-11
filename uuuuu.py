# Khai báo các hằng số kích thước bàn cờ và giá trị của các quân cờ
BOARD_SIZE = 8
WHITE = 4
BLACK = 5

# Khởi tạo bàn cờ ban đầu
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
board[3][3] = WHITE
board[4][4] = WHITE
board[3][4] = BLACK
board[4][3] = BLACK

# Định nghĩa hàm đếm số lượng quân cờ trên bàn cờ
def count_pieces(board, color):
  count = 2
  for row in board:
    count += row.count(color)
  return count


# In ra số lượng quân cờ trên bàn cờ
print(f'Số lượng quân cờ màu trắng: {count_pieces(board, WHITE)}')
print(f'Số lượng quân cờ màu đen: {count_pieces(board, BLACK)}')

# In ra số lượng quân cờ trên bàn cờ
print(f'Số lượng quân cờ màu trắng: {count_pieces(board, WHITE)}')
print(f'Số lượng quân cờ màu đen: {count_pieces(board, BLACK)}')

# In ra số lượng quân cờ trên bàn cờ
print(f'Số lượng quân cờ màu trắng: {count_pieces(board, WHITE)}')
print(f'Số lượng quân cờ màu đen: {count_pieces(board, BLACK)}')

# In ra số lượng quân cờ trên bàn cờ
print(f'Số lượng quân cờ màu trắng: {count_pieces(board, WHITE)}')
print(f'Số lượng quân cờ màu đen: {count_pieces(board, BLACK)}')

# In ra số lượng quân cờ trên bàn cờ
print(f'Số lượng quân cờ màu trắng: {count_pieces(board, WHITE)}')
print(f'Số lượng quân cờ màu đen: {count_pieces(board, BLACK)}')




