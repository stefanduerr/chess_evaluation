# import required module
import logging
import chess
import chess.pgn
from io import StringIO
import Classes as c
import numpy as np
import Evaluation as e
import chess.engine
from stockfish import Stockfish

stockfish = Stockfish(path="/Users/Mausezahn/Downloads/stockfish_15_win_x64_avx2/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 10, "Hash": 1024})
stockfish_low_depth = Stockfish(path="/Users/Mausezahn/Downloads/stockfish_15_win_x64_avx2/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe", depth=2, parameters={"Threads": 2, "Minimum Thinking Time": 10, "Hash": 1024})
stockfish_medium_depth = Stockfish(path="/Users/Mausezahn/Downloads/stockfish_15_win_x64_avx2/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe", depth=6, parameters={"Threads": 2, "Minimum Thinking Time": 10, "Hash": 1024})
# stockfish = Stockfish(path="/Users/zhelyabuzhsky/Work/stockfish/stockfish-9-64", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
# stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
# print(stockfish.get_best_move())

# def stockfish_evaluation(board, time_limit = 0.01):
#     engine = chess.engine.SimpleEngine.popen_uci("stockfish_10_x64")
#     result = engine.analyse(board, chess.engine.Limit(time=time_limit))
#     return result['score']

frm = '(%(lineno)d) %(message)s'
logging.basicConfig(format=frm, level=logging.DEBUG)

logger = logging.getLogger(__name__)

# create board object
chboard=chess.Board()
 
# display chess board
# logger.info(chboard)
# logger.info(chboard.legal_moves)
    # Evaluation = (material_eval + pi_sq_ta_score) / 100
    # logger.info(Evaluation)

# fen = "rqb2rk1/4bppp/p2ppn2/1p6/3BPPP1/2N2Q2/PPP4P/2KR1B1R w - - 0 14" tal

# fen = "r3k2r/ppp2pb1/4p1p1/3n2N1/1nBq4/1Q3PP1/PP1N3P/R1B1K2R w KQkq - 0 11" random pos
# fen = "r1br2k1/1pp2pp1/2n1pn1p/8/2PP4/qN3NP1/P3QPBP/R3R1K1 w - - 0 19" carlsen

# fen = "r2q1rk1/pbp1b1pp/1pn1Pn2/3p1P2/8/2NBBN2/PPP2PPP/R2Q1RK1 w - - 2 12"
fen = "3r2k1/3qpp2/3nbbpp/p7/1p3P2/6P1/PP2Q2P/R2R2K1 w - - 0 29"

# fen = "r2rb1k1/1pp2pp1/4p3/4P2p/2P3nP/1N4P1/P4PB1/R3R1K1 w - - 0 26"
# fen = "4rk2/7Q/2b1pq2/p1P5/1p1P4/1P1Bn3/P4PPP/5RK1 w - - 8 47"
# fen = "2k5/1p2p1p1/1p1p2p1/6P1/2P5/2P1P3/PP4K1/8 w - - 0 1"
# fen = "4k3/8/8/1r1p4/ppp5/PPPp4/1Q1P4/K7 w - - 0 1"
# fen = "n3r2k/4P1pp/8/1p6/8/8/PP3PPP/R4RK1 w Q - 1 15"
# fen = "rnb1k2r/1p3ppp/p1qppn2/8/3P4/2NB1N2/PPP2PPP/R2Q1RK1 w Qkq - 0 1"
# fen = "r1bqr1k1/pp1n1pbp/2pp1np1/4p3/2PP4/2NBPN2/PPQB1PPP/4RRK1 b - - 3 10"

pgn_string = """
[Event "IBM Kasparov vs. Deep Blue Rematch"]
[Site "New York, NY USA"]
[Date "1997.05.11"]
[Round "6"]
[White "Deep Blue"]
[Black "Kasparov, Garry"]
[Opening "Caro-Kann: 4...Nd7"]
[ECO "B17"]
[Result "1-0"]
 
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6
8.Nxe6 Qe7 9.O-O fxe6 10.Bg6+ Kd8 {Kasparov schüttelt kurz den Kopf}
11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6
17.Bf5 exf5 18.Rxe7 Bxe7 19.c4 1-0
"""

pgn = StringIO(pgn_string)
  
# Reading the game
game = chess.pgn.read_game(pgn)
game_result = game.headers['Result']

print("Game Result:", game_result)

# logger.info(game)
xboard = chess.Board(fen)
# logger.info('\n' + str(xboard))
tf_board = np.asarray((str(xboard)).split()).reshape(8,8)
# logger.info(xboard.legal_moves)

# e.evaluation(tf_board, xboard)

def player1(pos):
    moves = list(pos.legal_moves)
    turn = pos.turn
    movearr = {}
    movearr2 = []
    bestmoves = {}
    # logger.info(turn)
    print(len(list(pos.legal_moves)))
    stockfish_low_depth.set_fen_position(fen)
    Stockfish_Evaluation = stockfish_low_depth.get_evaluation()['value'] / 100
    stockfish_medium_depth.set_fen_position(fen)
    Stockfish_Evaluation_md = stockfish_medium_depth.get_evaluation()['value'] / 100
    
    for move in moves:
        newboard = pos.copy()
        conv_newboard = np.asarray((str(newboard)).split()).reshape(8,8)
        score_a, score_am, score_ax = e.evaluation(conv_newboard, newboard)
        newboard.push(move)
        
        opp_moves = list(newboard.legal_moves)

        stockfish.set_fen_position(newboard.fen())
        # logging.info(stockfish.get_best_move())
        best_move = chess.Move.from_uci(stockfish.get_best_move())
        newboard.push(best_move)
        newboard_arr = np.asarray((str(newboard)).split()).reshape(8,8)
        score, score_m, score_x = e.evaluation(newboard_arr, newboard)
        # movearr[str(move) + '_' + str(best_move)] = score
        movearr2.append([ score ,score_m, score_x, newboard.fen(), str(move) + '_' + str(best_move), score_a ,score_am, score_ax])

    movearr = {k: v for k, v in sorted(movearr.items(), key=lambda item: item[1])}
    movearr2.sort()

    print(movearr2[-1])
    prev_move = movearr2[-1][4]
    newpos = chess.Board(movearr2[-1][3])
    moves_2 = list(chess.Board(movearr2[-1][3]).legal_moves)
    movearr3 = []
    for move in moves_2:
        newboard = newpos.copy()
        conv_newboard = np.asarray((str(newboard)).split()).reshape(8,8)
        score_a, score_am, score_ax = e.evaluation(conv_newboard, newboard)
        newboard.push(move)
        
        # print(newboard, newboard.legal_moves)
        opp_moves = list(newboard.legal_moves)
        # bplusone = newboard.copy()
        # bplusone.push(omove)        
        # opp_moves.sort(key=lambda move: move.score, reverse=turn)
        
        
        # print(score_a, score_am, score_ax)
        # print(newboard.fen())
        stockfish.set_fen_position(newboard.fen())
        # logging.info(stockfish.get_best_move())
        best_move = chess.Move.from_uci(stockfish.get_best_move())
        newboard.push(best_move)
        newboard_arr = np.asarray((str(newboard)).split()).reshape(8,8)
        score, score_m, score_x = e.evaluation(newboard_arr, newboard)
        # movearr[str(move) + '_' + str(best_move)] = score
        movearr3.append([ score ,score_m, score_x, prev_move, str(move) + '_' + str(best_move), score_a ,score_am, score_ax]) 

    movearr3.sort()
    Final_Eval = 0
    # for i in range(3):
    #     Final_Eval = Final_Eval + movearr3[-(i+1)][0] * (1/(i+1)**2)
    #     print(Final_Eval)
    # Final_Eval = Final_Eval / (1 + 13/36)
    Final_Eval = movearr3[-1][0]
    return movearr3, Final_Eval, Stockfish_Evaluation, Stockfish_Evaluation_md
# print(player1(xboard))

def get_legal_moves(pos):
    moves = list(pos.legal_moves)
    turn = pos.turn
    movearr = {}
    movearr2 = []
    bestmoves = {}
    # logger.info(turn)
    print(len(list(pos.legal_moves)))
    return moves

movearr = {}
movearr2 = []

def evaluate_legal_moves(pos, move):

    newboard = pos.copy()
    conv_newboard = np.asarray((str(newboard)).split()).reshape(8,8)
    score_a, score_am, score_ax = e.evaluation(conv_newboard, newboard)
    newboard.push(move)
    
    # print(newboard, newboard.legal_moves)
    opp_moves = list(newboard.legal_moves)
    # bplusone = newboard.copy()
    # bplusone.push(omove)        
    # opp_moves.sort(key=lambda move: move.score, reverse=turn)
    
    
    # print(score_a, score_am, score_ax)
    # print(newboard.fen())
    stockfish.set_fen_position(newboard.fen())
    # logging.info(stockfish.get_best_move())
    best_move = chess.Move.from_uci(stockfish.get_best_move())
    newboard.push(best_move)
    newboard_arr = np.asarray((str(newboard)).split()).reshape(8,8)
    score, score_m, score_x = e.evaluation(newboard_arr, newboard)
    # movearr[str(move) + '_' + str(best_move)] = score
    movearr2.append([score_a ,score_am, score_ax, str(move) + '_' + str(best_move), score ,score_m, score_x])
    movearr2.sort()
    print(movearr2)
    # opp_moves = list(newboard.legal_moves)
    # for omove in opp_moves:
    #     boardplusone = newboard.copy()
    #     boardplusone.push(omove)
    #     boardplusone = np.asarray((str(boardplusone)).split()).reshape(8,8)


    #     if evaluation(conv_newboard) > evaluation(boardplusone):
    #         score = evaluation(boardplusone) 
    #         movearr[str(move) + '_' + str(omove)] = score

        # score_op = evaluation(boardplusone)
        # bestmoves[str(omove)] = score_op
        # bestmoves = {k: v for k, v in sorted(bestmoves.items(), key=lambda item: item[1])}



        # movearr.append([score, move, omove])           
    # go through board and return a score
    # newboard = np.asarray((str(newboard)).split()).reshape(8,8)
    # move.score = evaluation(newboard)
    # print(evaluation(newboard), move)
# moves.sort(key=lambda move: move.score, reverse=turn) # sort on score
# return moves[0].uci()
    # movearr = {k: v for k, v in sorted(movearr.items(), key=lambda item: item[1])}
    print(str(move) + ' finished!')

# print(f"{customer_group}{batch_code} {checksum:02} {id}")

if __name__ == "__main__":

    array_of_variations, CHEVA_Evaluation, Stockfish_Evaluation, Stockfish_Evaluation_md = player1(xboard)

    print('FEN of Examined Board:       ' + fen)
    print('CHEVAs Evaluation:           ' + str(CHEVA_Evaluation)) 
    print('Stockfishs Evaluation (d=1): ' + str(Stockfish_Evaluation))
    print('Stockfishs Evaluation (d=6): ' + str(Stockfish_Evaluation_md))
    print(array_of_variations)

    #Für bessere Performance wurde hier Multicore-Processing eingebaut.

    # move_arr = get_legal_moves(xboard)
    # print(move_arr)
    # func = partial(evaluate_legal_moves, xboard)
    # multiprocessing.freeze_support()
    # pool = multiprocessing.Pool(cores)
    # pool.map(func, move_arr)
    # print(movearr2)