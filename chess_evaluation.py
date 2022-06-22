import numpy as np
import Classes as c

print(c.lists.pawn_eval_dd)

# c.lists.c.lists.pawn_eval

def fen_transform_and_validate():
    numbers = np.array(range(1,9))
    numbers2 = []
    for z in numbers:
        numbers2.append(str(z))
    print(numbers2)

    start_position = "r3kb1r/pppqpppp/5n2/5b2/1P6/5NN1/P1PQPPPP/BR2K2R w Kkq - 0 1"
    print(start_position[44])

    counter = 0
    for j in range(len(start_position)):
        if start_position[j] == ' ' and counter == 0:
            side_to_move = start_position[j+1]
            counter = 1

    for x in range(len(start_position)):
        if start_position[x] in numbers2:
            print(str(x) + 'test')
            start_position = start_position.replace(start_position[x], int(start_position[x]) * '0')

    for i in range(1,8):
        if start_position[i*9-1] != '/':
            print(start_position)
            return False
    
    start_position = start_position.replace('/', '')
    return start_position, side_to_move



board = np.zeros(64, dtype='U1').reshape((8, 8))

testarr = []
testarr.extend(range(1,65))
# print(testarr)
# row = 7
# for i in range(64):
#     if start_position[i] == '/':
#         row -= 1   
            
#     board[row, i] = start_position[i]
fen_string, side_to_move = fen_transform_and_validate()

for i in range(8):
    for j in range(8):
        board[j,i] = fen_string[i+j*8]




d_board = board.flatten()
print(d_board)

# array = {"pawn": 0, "knight": 1, "bishop": 2}
# array2 = ["pawn", "knight", "bishop"]

# def function(eval_number, eval_numberb, eval_array):
#     for i in range(64):
#             if d_board[i] == 'P':
#                 eval_number += eval_array[i]
#             elif d_board[i] == 'p':
#                 eval_numberb += np.flipud(eval_array)[i]    


# function(c.lists.pawn_eval_number, c.lists.pawn_eval_numberb, c.lists.pawn_eval)
# function(c.lists.knight_eval_number, c.lists.knight_eval_numberb, c.lists.knight_eval)
# function(c.lists.bishop_eval_number, c.lists.bishop_eval_numberb, c.lists.bishop_eval)

for i in range(64):
    if d_board[i] == 'P':
        c.lists.pawn_eval_number += c.lists.pawn_eval[i]
    elif d_board[i] == 'p':
        c.lists.pawn_eval_numberb += np.flipud(c.lists.pawn_eval)[i]

for i in range(64):
    if d_board[i] == 'N':
        c.lists.knight_eval_number += c.lists.knight_eval[i]
    elif d_board[i] == 'n':
        c.lists.knight_eval_numberb += np.flipud(c.lists.knight_eval)[i]

for i in range(64):
    if d_board[i] == 'B':
        c.lists.bishop_eval_number += c.lists.bishop_eval[i]
    elif d_board[i] == 'b':
        c.lists.bishop_eval_numberb += np.flipud(c.lists.bishop_eval)[i]

for i in range(64):
    if d_board[i] == 'Q':
        c.lists.queen_eval_number += c.lists.queen_eval[i]
    elif d_board[i] == 'q':
        c.lists.queen_eval_numberb += np.flipud(c.lists.queen_eval)[i]

for i in range(64):
    if d_board[i] == 'R':
        c.lists.rook_eval_number += c.lists.rook_eval[i]
    elif d_board[i] == 'r':
        c.lists.rook_eval_numberb += np.flipud(c.lists.rook_eval)[i]

for i in range(64):
    if d_board[i] == 'K':
        c.lists.king_eval_number += c.lists.king_eval[i]
    elif d_board[i] == 'k':
        c.lists.king_eval_numberb += np.flipud(c.lists.king_eval)[i]


pawn_score = c.lists.pawn_eval_number - c.lists.pawn_eval_numberb
knight_score = c.lists.knight_eval_number - c.lists.knight_eval_numberb
bishop_score = c.lists.bishop_eval_number - c.lists.bishop_eval_numberb
rook_score = c.lists.rook_eval_number - c.lists.rook_eval_numberb
queen_score = c.lists.queen_eval_number - c.lists.queen_eval_numberb
king_score = c.lists.king_eval_number - c.lists.king_eval_numberb


print(pawn_score, knight_score, bishop_score, rook_score, queen_score, king_score)
pi_sq_ta_score = pawn_score + knight_score + bishop_score + rook_score + queen_score + king_score


print('pawn score:' + str(c.lists.pawn_eval_number))
print('pawn score black:' + str(c.lists.pawn_eval_numberb))
print('knight score:' + str(c.lists.knight_eval_number))
print('knight score black:' + str(c.lists.knight_eval_numberb))
print('bishop score:' + str(c.lists.bishop_eval_number))
print('bishop score black:' + str(c.lists.bishop_eval_numberb))
print('rook score:' + str(c.lists.rook_eval_number))
print('rook score black:' + str(c.lists.rook_eval_numberb))
print('queen score:' + str(c.lists.queen_eval_number))
print('queen score black:' + str(c.lists.queen_eval_numberb))
print('king score:' + str(c.lists.king_eval_number))
print('king score black:' + str(c.lists.king_eval_numberb))


print(board)

material_eval = 0

for i in range(8):
    for j in range(8):
        if board[i,j] in c.lists.piece_dict:
            material_eval += c.lists.piece_dict[board[i,j]]

print(material_eval)

Evaluation = (material_eval + pi_sq_ta_score) / 100

print(Evaluation, side_to_move)

# if __name__ == "__main__":
#     print(board)