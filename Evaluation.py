import chess
import chess.engine
import chess.pgn
import Classes as c
import numpy as np
from stockfish import Stockfish
import logging

stockfish = Stockfish(path="/Users/Mausezahn/Downloads/stockfish_15_win_x64_avx2/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe", depth=14, parameters={"Threads": 2, "Minimum Thinking Time": 10, "Hash": 1024})
frm = '(%(lineno)d) %(message)s'
logging.basicConfig(format=frm, level=logging.DEBUG)
logger = logging.getLogger(__name__)

### CHEVA: EVALUIERUNGSFUNKTION ###
def evaluation(pos_arr, position): #Parameter: numpy-2D-Array, chess.Board()-Variable

    # Wichtige Variablen
    Evaluation, Evaluation_m, Evaluation_x = 0, 0, 0    
    material_eval = 0
    pi_sq_ta_score = 0
    c.lists.pawn_eval_number = 0
    c.lists.pawn_eval_numberb = 0
    c.lists.knight_eval_number = 0
    c.lists.knight_eval_numberb = 0
    c.lists.bishop_eval_number = 0
    c.lists.bishop_eval_numberb = 0
    c.lists.rook_eval_number = 0
    c.lists.rook_eval_numberb = 0
    c.lists.queen_eval_number = 0
    c.lists.queen_eval_numberb = 0
    c.lists.king_eval_number = 0
    c.lists.king_eval_numberb = 0

    ### EVALUIERUNGSFUNKTION START ###

    # Material
    for i in range(8):
        for j in range(8):
            if pos_arr[i,j] in c.lists.piece_dict:
                material_eval += c.lists.piece_dict[pos_arr[i,j]]

    # Felder der Figuren
    for i in range(64):
        match pos_arr.flatten()[i]:
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
    
    # Bauernstruktur
    doubled_pawns_w = 0
    doubled_pawns_b = 0
    blpawns_w = 0
    blpawns_b = 0

    for file in chess.FILE_NAMES:
        count_w = 0
        count_b = 0
        for rank in chess.RANK_NAMES:
            
            if position.piece_at(chess.parse_square(file + rank)) is not None:

                if position.piece_at(chess.parse_square(file + rank)).symbol() == 'P':
                    count_w += 1

                    if position.piece_at(chess.parse_square(file + str(int(rank)+1))) is not None:
                        blpawns_w += 1

                if position.piece_at(chess.parse_square(file + rank)).symbol() == 'p':
                    count_b += 1

                    if position.piece_at(chess.parse_square(file + str(int(rank)-1))) is not None:
                        blpawns_b += 1

            if count_w > 1:
                doubled_pawns_w += 1
                count_w = 0
            if count_b > 1:
                doubled_pawns_b += 1
                count_b = 0

    # Mobilität
    if position.turn == chess.WHITE:
        list_side_a = list(position.legal_moves)
        position.turn = chess.BLACK
        list_side_b = list(position.legal_moves)
        position.turn = chess.WHITE
    elif position.turn == chess.BLACK:
        list_side_b = list(position.legal_moves)
        position.turn = chess.WHITE
        list_side_a = list(position.legal_moves)
        position.turn = chess.BLACK

    # Ausrechnung der Werte (Mobilität, Bauernstruktur, Felder der Figuren)
    mobility_score = len(list_side_a) - len(list_side_b)    
    doubled_blocked_pawn_score = (doubled_pawns_w - doubled_pawns_b + blpawns_w - blpawns_b)
    pi_sq_ta_score = pawn_score + knight_score + bishop_score + rook_score + queen_score + king_score

    # Berechnung der Stellungsbewertung, Gewichtung der Kriterien
    Evaluation_m = ((material_eval + pi_sq_ta_score) / 100) + mobility_score / 750 - doubled_blocked_pawn_score / 100
    
    # Kontrollwert 1 ohne Bauernstruktur
    Evaluation = ((material_eval + pi_sq_ta_score) / 100) + (mobility_score / 750)
    
    # Kontrollwert 2 ohne Bauernstruktur und Mobilität
    Evaluation_x = ((material_eval + pi_sq_ta_score) / 100)

    # gibt Stellungsbewertung, Kontrollwert 1 und Kontrollwert 2 zurück
    return Evaluation_m, Evaluation, Evaluation_x
    
    ### EVALUIERUNGSFUNKTION ENDE ###