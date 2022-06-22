from cgi import test
from tracemalloc import start
import numpy as np


piece_dict = {
    'r': -500,
    'n': -320,
    'b': -330,
    'q': -900,
    'k': -20000,
    'p': -100,
    'P': 100,
    'R': 500,
    'N': 320,
    'B': 330,
    'Q': 900,
    'K': 20000,
}

def transform_and_validate():
    numbers = np.array(range(1,9))
    numbers2 = []
    for z in numbers:
        numbers2.append(str(z))
    print(numbers2)

    start_position = "r3kb1r/pppqpppp/5n2/5b2/1P3B2/2N2N2/P1PQPPPP/R3K2R w KQkq - 0 1"
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
fen_string, side_to_move = transform_and_validate()

for i in range(8):
    for j in range(8):
        board[j,i] = fen_string[i+j*8]


print(board)

material_eval = 0

for i in range(8):
    for j in range(8):
        if board[i,j] in piece_dict:
            material_eval += piece_dict[board[i,j]]

print(material_eval, side_to_move)

# if __name__ == "__main__":
#     print(board)