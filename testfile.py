import chess
import matplotlib.pyplot as plt

# fen = "2k5/1p2p1p1/1p1p2p1/6P1/2P1P3/2P5/PP4K1/8 b - - 0 1"
fen = "k7/p1p3p1/p1p2pp1/b1P2p2/P2P1P2/1P1P1P2/1P4K1/8 w - - 0 1"
chboard=chess.Board(fen)

# print(chess.SQUARES(chboard[0]))

# print(type(chboard.piece_at(chess.parse_square('a1'))))
# print(type(chess.PAWN))
arr = [[-7.160666666666667, -7.1706666666666665, -7.1, 'd2e4_a7a5', 'b3d3_b4d3', 2.0246666666666666, 2.0246666666666666, 2.05], [-7.014666666666667, -7.024666666666667, -6.95, 'd2e4_a7a5', 'b3c2_b4c2', 2.0246666666666666, 2.0246666666666666, 2.05], [-6.978666666666667, -6.988666666666667, -6.95, 'd2e4_a7a5', 'b3e3_d5e3', 2.0246666666666666, 2.0246666666666666, 2.05], [-6.928666666666667, -6.938666666666667, -6.9, 'd2e4_a7a5', 'b3c3_d5c3', 2.0246666666666666, 2.0246666666666666, 2.05], [-3.620666666666667, -3.630666666666667, -3.6, 'd2e4_a7a5', 'b3b4_d5b4', 2.0246666666666666, 2.0246666666666666, 2.05], [-2.872, -2.872, -2.8, 'd2e4_a7a5', 'h1g1_d4g1', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.5233333333333332, -1.5233333333333332, -1.45, 'd2e4_a7a5', 'c4d3_b4d3', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.4746666666666666, -1.4846666666666666, -1.45, 'd2e4_a7a5', 'b3d1_d4c4', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.422, -1.432, -1.4, 'd2e4_a7a5', 'e4f6_g7f6', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.328, -1.328, -1.3, 'd2e4_a7a5', 'c4a6_a8a6', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.294, -1.294, -1.25, 'd2e4_a7a5', 'e4c3_d5c3', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.2746666666666666, -1.2846666666666666, -1.25, 'd2e4_a7a5', 'e4d6_c7d6', 2.0246666666666666, 2.0246666666666666, 2.05], [-1.226, -1.226, -1.15, 'd2e4_a7a5', 'c1e3_d4e3', 2.0246666666666666, 2.0246666666666666, 2.05], 
[-0.1366666666666667, -0.12666666666666668, -0.1, 'd2e4_a7a5', 'g5e6_f7e6', 2.0246666666666666, 2.0246666666666666, 2.05], [0.8666666666666667, 0.8666666666666667, 0.9, 'd2e4_a7a5', 'a2a4_h8h2', 2.0246666666666666, 2.0246666666666666, 2.05], [0.8693333333333334, 0.8693333333333334, 0.9, 'd2e4_a7a5', 'e4c5_h8h2', 2.0246666666666666, 2.0246666666666666, 2.05], [1.5213333333333334, 1.5313333333333334, 1.55, 'd2e4_a7a5', 'g5h7_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.6019999999999999, 1.6219999999999999, 1.65, 'd2e4_a7a5', 'g5h3_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.7693333333333334, 1.7693333333333334, 1.8, 'd2e4_a7a5', 'e4f2_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.772, 1.772, 1.8, 'd2e4_a7a5', 'c4f1_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.8126666666666666, 1.8126666666666666, 1.85, 'd2e4_a7a5', 'e4d2_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.8373333333333335, 1.8273333333333335, 1.85, 'd2e4_a7a5', 'c4d5_e6d5', 2.0246666666666666, 2.0246666666666666, 2.05], [1.8719999999999999, 1.8719999999999999, 1.9, 'd2e4_a7a5', 'c4e2_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.8793333333333333, 1.8793333333333333, 1.95, 'd2e4_a7a5', 'b3a3_b4c2', 2.0246666666666666, 2.0246666666666666, 2.05], [1.9246666666666665, 1.9246666666666665, 1.95, 'd2e4_a7a5', 'h2h4_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.9693333333333334, 1.9693333333333334, 2.0, 'd2e4_a7a5', 'h1f1_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.9706666666666666, 1.9706666666666666, 2.0, 'd2e4_a7a5', 'a1b1_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.9706666666666666, 1.9706666666666666, 2.0, 'd2e4_a7a5', 'e1e2_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.9706666666666666, 1.9706666666666666, 2.0, 'd2e4_a7a5', 'h2h3_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [1.9733333333333334, 1.9733333333333334, 2.0, 'd2e4_a7a5', 'a2a3_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [2.010666666666667, 2.0206666666666666, 2.05, 'd2e4_a7a5', 'g3g4_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [2.0693333333333332, 2.0693333333333332, 2.1, 'd2e4_a7a5', 'e1f1_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [2.072, 2.072, 2.1, 'd2e4_a7a5', 'f3f4_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [2.078666666666667, 2.078666666666667, 2.1, 'd2e4_a7a5', 'c1d2_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [2.1660000000000004, 2.176, 2.2, 'd2e4_a7a5', 'c1f4_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05], [2.1813333333333333, 2.1813333333333333, 2.2, 'd2e4_a7a5', 'c4b5_c7c6', 2.0246666666666666, 2.0246666666666666, 2.05], [2.2, 2.18, 2.2, 'd2e4_a7a5', 'b3a4_c7c6', 2.0246666666666666, 2.0246666666666666, 2.05], [3.02, 3.03, 3.05, 'd2e4_a7a5', 'g5f7_a5a4', 2.0246666666666666, 2.0246666666666666, 2.05]]
print(chboard.piece_at(chess.H8))

# Final_Eval = 0
# for i in range(3):
#     Final_Eval = Final_Eval + arr[-(i+1)][0] * (1/(i+1)**2)
#     print(Final_Eval)
# Final_Eval = Final_Eval / (1 + 13/36)
# print(Final_Eval)
# count = 0
# doubled_pawns_w = 0
# doubled_pawns_b = 0
import matplotlib.pyplot as plt
import numpy as np

Sg = [5.53, 0.35, -8.91]
Sm = [4.39, 0.81, -11.79]
Ch = [3.24, 0.69, -6.95]
axis = ['Position 1:\nBauernallianz', 'Position 2:\nCarlsen vs. Nepomniatchtchi',  'Position 3:\nSchwarze ??bermacht']
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(Sg)) 
print(x) # the label locations
width = 0.30  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-0.3, Sg, width, label='Stockfish (Tiefe=1)')
rects2 = ax.bar(x, Sm, width, label='Stockfish (Tiefe=6)')
rects3 = ax.bar(x+0.3, Ch, width, label='CHEVA v2.0')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Bewertung')
ax.set_title('CHEVA vs. Stockfish')
ax.set_xticks(x, axis)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()
# blpawns_w = 0
# blpawns_b = 0


# plt.bar(axis, Sm, axis, Ch, axis, Sg)
# plt.show()
# for file in chess.FILE_NAMES:
#     count_w = 0
#     count_b = 0
#     for rank in chess.RANK_NAMES:
        
#         if chboard.piece_at(chess.parse_square(file + rank)) is not None:

#             if chboard.piece_at(chess.parse_square(file + rank)).symbol() == 'P':
#                 count_w += 1

#                 if chboard.piece_at(chess.parse_square(file + str(int(rank)+1))) is not None:
#                     blpawns_w += 1

#             if chboard.piece_at(chess.parse_square(file + rank)).symbol() == 'p':
#                 count_b += 1

#                 if chboard.piece_at(chess.parse_square(file + str(int(rank)-1))) is not None:
#                     blpawns_b += 1

#         if count_w > 1:
#             doubled_pawns_w += 1
#             count_w = 0
#         if count_b > 1:
#             doubled_pawns_b += 1
#             count_b = 0

# doubled_blocked_pawn_score = (doubled_pawns_w - doubled_pawns_b + blpawns_w - blpawns_b) / 100
# print(doubled_blocked_pawn_score)