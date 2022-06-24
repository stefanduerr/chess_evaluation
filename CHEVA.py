# import required module
import chess
import chess.pgn
from io import StringIO
import Classes as c
import numpy as np
from Evaluation import evaluation

# create board object
chboard=chess.Board()
 
# display chess board
print(chboard)
print(chboard.legal_moves)


    # Evaluation = (material_eval + pi_sq_ta_score) / 100
    # print(Evaluation)


fen = "rnb1k2r/1p3ppp/p1qppn2/8/3P4/2NB1N2/PPP2PPP/R2Q1RK1 b Qkq - 0 1"
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

print(game)
xboard = chess.Board(fen)
print(xboard)
tf_board = np.asarray((str(xboard)).split()).reshape(8,8)
print(xboard.legal_moves)

evaluation(tf_board)