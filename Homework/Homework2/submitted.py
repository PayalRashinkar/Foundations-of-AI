import math
import sys

line = []
with open('input.txt', 'r') as input_file:
        for every_line in input_file:
                line.append(every_line)

my_color = line[0].split()
if my_color[0] == 'WHITE':
        iAm = 'w'
else:
        iAm = 'b'


time_left1 = line[1].split('.')
time_left = map(int, time_left1)
time, dec = time_left

tmp_cap = line[2].split(',')
capture = map(int, tmp_cap)
wcapture, bcapture = capture

if iAm == 'w':
    p_cap_count = wcapture
    o_cap_count = bcapture
else:
    p_cap_count = bcapture
    o_cap_count = wcapture

board = []

for i, grid in enumerate(line):
        if i >= 3 and i <= 21:
            row = map(str, grid.strip().split())
            row_new = [char for string in row for char in string]
            board.append(row_new)

white = 0
black = 0
for r in board:
        white += r.count('w')
        black += r.count('b')

def write_to_file(move):
        rows = ['19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1']
        cols = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T']
        grid = [[f"{row}{col}" for col in cols] for row in rows]
        cell = grid[move[0]][move[1]]
        with open("output.txt","w") as output:
            output.write(cell)
        sys.exit()


def look_up(board, move):
    
    x, y = move
    for row in board:
        row_str = ''.join(row)
        if 'wwwww' in row_str:
            write_to_file(move)
        elif 'bbbbb' in row_str:
            write_to_file(move)
    
    for col in range(len(board[0])):
        column_str = ''.join([board[row][col] for row in range(len(board))])
        if 'wwwww' in column_str:
            write_to_file(move)
        elif 'bbbbb' in column_str:
            write_to_file(move)

    for start_row in range(len(board)-4):
        for start_col in range(len(board[0])-4):
            diagonal_str = ''.join([board[start_row+i][start_col+i] for i in range(5)])
            if 'wwwww' in diagonal_str:
                write_to_file(move)
            elif 'bbbbb' in diagonal_str:
                write_to_file(move)

    for start_row in range(4, len(board)):
        for start_col in range(len(board[0])-4):
            diagonal_str = ''.join([board[start_row-i][start_col+i] for i in range(5)])
            if 'wwwww' in diagonal_str:
                write_to_file(move)
            elif 'bbbbb' in diagonal_str:
                write_to_file(move)
    
    if iAm == 'w' and board[x][y] == iAm:
        player = 'w'
        opponent = 'b'
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and board[x+dx][y+dy] == player and board[x+2*dx][y+2*dy] == player and board[x+3*dx][y+3*dy] == opponent:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x+3*dx][y+3*dy] == player:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            #if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and x + 4 * dx < 19 and y + 4 * dy < 19 and board[x+dx][y+dy] == player and board[x+2*dx][y+2*dy] == player and board[x+3*dx][y+3*dy] == player and board[x+4*dx][y+4*dy] == '.':
            if x + 2 * dx < 19 and y + 2 * dy < 19 and board[x+dx][y+dy] == player and board[x+2*dx][y+2*dy] == player and board[x+3*dx][y+3*dy] == player:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and x + 4 * dx < 19 and y + 4 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x+3*dx][y+3*dy] == opponent and board[x+4*dx][y+4*dy] == '.':
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x - 2 * dx < 19 and y - 2 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x-dx][y-dy] == opponent and board[x-2*dx][y-2*dy] == opponent:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x - dx < 19 and y - dy < 19 and board[x-dx][y-dy] == opponent and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and x + 4 * dx < 19 and y + 4 * dy < 19 and x + 5 * dx < 19 and y + 5 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x+3*dx][y+3*dy] == opponent and board[x+4*dx][y+4*dy] == opponent and board[x+5*dx][y+5*dy] == player:
                write_to_file(move)

    elif iAm == 'b' and board[x][y] == iAm:
        player = 'b'
        opponent = 'w'
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and board[x+dx][y+dy] == player and board[x+2*dx][y+2*dy] == player and board[x+3*dx][y+3*dy] == opponent:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x+3*dx][y+3*dy] == player:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and x + 4 * dx < 19 and y + 4 * dy < 19 and board[x+dx][y+dy] == player and board[x+2*dx][y+2*dy] == player and board[x+3*dx][y+3*dy] == player and board[x+4*dx][y+4*dy] == '.':
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and x + 4 * dx < 19 and y + 4 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x+3*dx][y+3*dy] == opponent and board[x+4*dx][y+4*dy] == '.':
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x - 2 * dx < 19 and y - 2 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x-dx][y-dy] == opponent and board[x-2*dx][y-2*dy] == opponent:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x - dx < 19 and y - dy < 19 and board[x-dx][y-dy] == opponent and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent:
                write_to_file(move)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            if x + 2 * dx < 19 and y + 2 * dy < 19 and x + 3 * dx < 19 and y + 3 * dy < 19 and x + 4 * dx < 19 and y + 4 * dy < 19 and x + 5 * dx < 19 and y + 5 * dy < 19 and board[x+dx][y+dy] == opponent and board[x+2*dx][y+2*dy] == opponent and board[x+3*dx][y+3*dy] == opponent and board[x+4*dx][y+4*dy] == opponent and board[x+5*dx][y+5*dy] == player:
                write_to_file(move)
    
    
    if all([cell != '.' for row in board for cell in row]):
        return True, 'Draw'
    

    return False
    


def make_move(state, move, player):
    i, j = move
    new_state = [row[:] for row in state]
    new_state[i][j] = player
    return new_state

def attack_defense(state, player):
    # Define weights for different features
    if player == 'w':
        opponent = 'b'
    else:
        opponent = 'w'
    captures = [0, 0]
    for i in range(19):
        for j in range(19):
            if state[i][j] == player:
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
                    if i + 2 * di < 19 and j + 2 * dj < 19 and i + 3 * di < 19 and j + 3 * dj < 19 and state[i+di][j+dj] == opponent and state[i+2*di][j+2*dj] == opponent and state[i+3*di][j+3*dj] == player:
                        captures[0] += 1
                    
            elif state[i][j] == opponent:
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
                    if i + 2 * di < 19 and j + 2 * dj < 19 and i + 3 * di < 19 and j + 3 * dj < 19 and state[i+di][j+dj] == player and state[i+2*di][j+2*dj] == player and state[i+3*di][j+3*dj] == opponent:
                        captures[1] += 1
    return captures


def five_in_r_c_d(state, play_opp):
    formations = 0
    for i in range(19):
        for j in range(19):
            for di, dj in [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]:
                if i + 4 * di < 19 and j + 4 * dj < 19 and all(state[i+k*di][j+k*dj] == play_opp for k in range(5)):
                    formations += 1
    return formations


def four_in_r_c_d(state, play_opp):
    if play_opp == 'w':
        opponent = 'b'
    else:
        opponent = 'w'
    threats4 = 0
    for i in range(19):
        for j in range(19):
             for di, dj in [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]:
                if i + 4 * di < 19 and j + 4 * dj < 19:
                    row = [state[i+k*di][j+k*dj] for k in range(5)]
                    if row.count(play_opp) == 4 and row.count(opponent) == 1:
                        threats4 += 1
    return threats4


def othree_in_r_c_d(state, play_opp):
    threatso3 = 0
    for i in range(19):
        for j in range(19):
             for di, dj in [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]:
                if i + 4 * di < 19 and j + 4 * dj < 19:
                    row = [state[i+k*di][j+k*dj] for k in range(5)]
                    if row.count(play_opp) == 3 and row.count('.') == 2:
                        threatso3 += 1
    return threatso3


def generate_moves(state, play_opp):
    moves = []
    for i in range(19):
        for j in range(19):
            if state[i][j] == '.':
                for di, dj in [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]:
                    if (i+di >= 0 and i+di < 19 and j+dj >= 0 and j+dj < 19) and (state[i+di][j+dj] == 'w' or state[i+di][j+dj] == 'b'):
                    #if (i+di >= 0 and i+di < 19 and j+dj >= 0 and j+dj < 19) and state[i+di][j+dj] == play_opp:
                            moves.append((i, j))
                            break
    return moves

def generate_moves_eval(state, play_opp):
    moves = []
    for i in range(19):
        for j in range(19):
            if state[i][j] == '.':
                for di, dj in [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]:
                    if (i+di >= 0 and i+di < 19 and j+dj >= 0 and j+dj < 19) and state[i+di][j+dj] == play_opp:
                            moves.append((i, j))
                            break
    return moves 


def utility_func(state, player):
    if player == 'w':
        opponent = 'b'
    else:
        opponent = 'w'

    capture_weight = 2000
    formation_weight = 100000
    threat_weight_4 = 9000
    threat_weight_o3 = 3000
    mobility_weight = 0.1
    
     
    captures = attack_defense(state, player)
    capture_score = capture_weight * (captures[0] - captures[1]) 

    formation_score = formation_weight * (five_in_r_c_d(state, player) - five_in_r_c_d(state, opponent))
    
    threat_score_4 = threat_weight_4 * four_in_r_c_d(state, opponent)

    threat_score_o3 = threat_weight_o3 * (othree_in_r_c_d(state, player) - othree_in_r_c_d(state, opponent))
    
    mobility_score = mobility_weight * (len(generate_moves_eval(state, player)) - len(generate_moves_eval(state, opponent)))
    
    return capture_score + formation_score + threat_score_4 + threat_score_o3 + mobility_score


def alpha_beta(state, depth, alpha, beta, maximizing_player, player):
    if player == 'w':
        opponent = 'b' 
    else:       
        opponent = 'w'

    if depth == 0:
        score = utility_func(state, player)
        return score, None
   

    moves = generate_moves(state, player)
    if len(moves) == 0:
        score = utility_func(state, player)
        return score, None
    
    if maximizing_player:
        moves = sorted(moves, key=lambda move: utility_func(make_move(state, move, player), player), reverse=True)
    else:
        moves = sorted(moves, key=lambda move: utility_func(make_move(state, move, player), player))
   
    best_move = None
    
    for move in moves:
        new_state = make_move(state, move, player)

        if look_up(new_state, move) == 20:
            write_to_file(move)

        if iAm == 'w':
            score, _ = alpha_beta(new_state, depth-1, alpha, beta, False if player == 'w' else True, opponent)
        else:
            score, _ = alpha_beta(new_state, depth-1, alpha, beta, False if player == 'b' else True, opponent)
	
        
        if maximizing_player:
            if score > alpha:
                alpha = score
                best_move = move
        else:
            if score < beta:
                beta = score
                best_move = move
        
        if beta <= alpha:
            break
    
    if maximizing_player:
        return alpha, best_move
    else:
        return beta, best_move

def iterative_dfs(state, max_depth):
	for depth in range(1, max_depth+1):
		_, move = alpha_beta(state, depth, -math.inf, math.inf, True, iAm)
	return move


                
if board[9][9] == '.' and black == 0:
        with open("output.txt","w") as output:
                output.write("10K")
elif (white == 1 and black == 1 and iAm == 'w') or (board[9][9] == 'w' and black == 0 and iAm == 'b'):
        if board[9][6] == '.' and iAm == 'w':
            with open("output.txt","w") as output:
                output.write("10G")
        elif board[9][6] == 'b' and iAm == 'w':
            with open("output.txt","w") as output:
                output.write("10N")
        elif iAm == 'b':
            with open("output.txt","w") as output:
                output.write("12K")
else:
	if time >= 100:
		move = iterative_dfs(board, 3)
	elif time < 100 and time >= 5:
		move = iterative_dfs(board, 2)
	elif time < 5:
		move = iterative_dfs(board, 1)
        
	write_to_file(move)

