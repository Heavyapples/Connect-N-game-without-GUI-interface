# GLOBAL VARIABLES
N = 5
num_row = N + 3
num_col = N + 2
disk = ['\u2B1C', '\u26AA', '\u26AB']
board = []

def init_board(n):
    '''initialise the board'''
    global N, num_row, num_col
    N = n
    num_row = n + 3
    num_col = n + 2
    for c in range(num_col):
        board.append([0]*num_row)
    
def display():
    '''print the board'''
    to_print = "    "
    for i in range(num_col):
        to_print = to_print + f'[{i}]'
    print(to_print)
    for i in range(num_row):
        to_print = f'[{i:2}]'
        for j in range(num_col):
            to_print = f'{to_print}{disk[board[j][i]]:2}'
        print(to_print)

def game():
    '''play the game'''
    n = input('Please input N:')
    init_board(int(n))
    
    p = 0
    while True:
        c = input(f'Player {p} select column:')
        if c == 'q': # quit the game
            print(f'Player {p} resigned')
            break
            
        # drop disk    
        f = drop_disk(int(c), p+1)
        if f == 0: # illegal move
            print(f'Column {c} is an illegal move')
            continue            
        display()
        
        # check winner and switch side
        if have_winner():
            print(f'Player {p} won')
            break
        p = (p + 1)%2

def drop_disk(col, player):
    '''在列col为给定玩家放置一个棋子'''
    # 检查给定的列是否超出了边界
    if col < 0 or col >= num_col:
        return 0
    
    # 从列的底部开始查找第一个空槽，并将玩家的棋子放置在那里
    for row in range(num_row-1, -1, -1):
        if board[col][row] == 0:
            board[col][row] = player
            return 1
    
    # 如果该列已满，则返回0表示移动不成功
    return 0

def check_line(line):
    '''检查给定行、列或对角线上是否有N个连续的相同颜色的棋子'''
    # 将第一个棋子作为线的一部分
    count = 1
    
    # 遍历线的其余部分，查找相同颜色的连续棋子
    for i in range(1, len(line)):
        if line[i] == line[i - 1] and line[i] != 0:
            count += 1
            if count == N:
                return True
        else:
            count = 1
    
    # 如果没有找到连续的棋子，则返回False
    return False

def have_winner():
    '''检查是否存在获胜者'''
    # 检查所有行是否存在获胜者
    for row in range(num_row):
        if check_line([board[col][row] for col in range(num_col)]):
            return True
    
    # 检查所有列是否存在获胜者
    for col in range(num_col):
        if check_line([board[col][row] for row in range(num_row)]):
            return True
    
    # 检查所有对角线是否存在获胜者
    for diag in range(-num_row + N, num_col - N + 1):
        if check_line([board[col][col + diag] for col in range(max(0, -diag), min(num_row - diag, num_col))]):
            return True
        
        if check_line([board[col][num_row - col - diag - 1] for col in range(max(0, -diag), min(num_row - diag, num_col))]):
            return True
    
    # 如果没有获胜者，则返回False
    return False


game()