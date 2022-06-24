import chess
import chess.pgn
from io import StringIO
import Classes as c
import numpy as np

def evaluation(position):
    
    material_eval = 0

    for i in range(8):
        for j in range(8):
            if position[i,j] in c.lists.piece_dict:
                material_eval += c.lists.piece_dict[position[i,j]]

    for i in range(64):
        match position.flatten()[i]:
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

    pi_sq_ta_score = pawn_score + knight_score + bishop_score + rook_score + queen_score + king_score
    Evaluation = (material_eval + pi_sq_ta_score) / 100
    print(Evaluation, material_eval, pi_sq_ta_score)