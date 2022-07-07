import numpy as np
import Classes as c
# import required module
import chess
 
# create board object
chboard=chess.Board()
 
# display chess board
print(str(chboard))


def fen_transform_and_validate():
    conversion_array = np.array(range(1,9))
    helping_array = []
    for z in conversion_array:
        helping_array.append(str(z))
    start_position = "8/8/3p4/3R4/8/8/8/8 w - - 0 1"
    counter = 0

    for j in range(len(start_position)):
        if start_position[j] == ' ' and counter == 0:
            side_to_move = start_position[j+1]
            counter = 1

    while len(start_position) < 80:
        for x in range(len(start_position)):
            if start_position[x] in helping_array:
                start_position = start_position.replace(start_position[x], int(start_position[x]) * '0')

    for i in range(1,8):
        if start_position[i*9-1] != '/':
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



def material_and_piece_square_eval(board):
    d_board = board.flatten()
    print('row66' + str(d_board))

    for i in range(64):
        match d_board[i]:
            case 'P':
                c.lists.pawn_eval_number += c.lists.pawn_eval[i]
            case 'p':
                c.lists.pawn_eval_numberb += np.flipud(c.lists.pawn_eval)[i]
            case 'N':
                c.lists.knight_eval_number += c.lists.knight_eval[i]
            case 'n':
                c.lists.knight_eval_numberb += np.flipud(c.lists.knight_eval)[i]
            case 'B':
                c.lists.bishop_eval_number += c.lists.bishop_eval[i]
            case 'b':
                c.lists.bishop_eval_numberb += np.flipud(c.lists.bishop_eval)[i]
            case 'Q':
                c.lists.queen_eval_number += c.lists.queen_eval[i]
            case 'q':
                c.lists.queen_eval_numberb += np.flipud(c.lists.queen_eval)[i]
            case 'R':
                c.lists.rook_eval_number += c.lists.rook_eval[i]
            case 'r':
                c.lists.rook_eval_numberb += np.flipud(c.lists.rook_eval)[i]
            case 'K':
                c.lists.king_eval_number += c.lists.king_eval[i]
            case 'k':
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
    material_eval = 0

    for i in range(8):
        for j in range(8):
            if board[i,j] in c.lists.piece_dict:
                material_eval += c.lists.piece_dict[board[i,j]]

    print(material_eval)
    Evaluation = (material_eval + pi_sq_ta_score) / 100
    print(Evaluation)
    print(chboard.legal_moves)

def moveislegal(fs, s_tomove, piece_type):
    allowed_sq = []
    for i in range(-8, 8):
        if s_tomove == fs + i*8 and 0 < s_tomove < 64:
            return True
        if s_tomove == fs + i:
            hboard = board
            
            return True       
    return False
print(board)
piece_type = 0

def move_system():
    fsquare = int(input())
    s_to_move = int(input())

    mboard = board.flatten()
    if moveislegal(fsquare, s_to_move, piece_type):
        mboard[int(s_to_move)] = mboard[int(fsquare)]
        mboard[int(fsquare)] = 0
    else:
        print('Illegal Move!')

    mboard = mboard.reshape(8, 8)
    print(mboard)




# if __name__ == "__main__":
#     print(board)