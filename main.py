import chess
import agent


def get_state(board_str):
    pieces_dict = {'.': 0, 'r': 1, 'n': 2, 'b': 3, 'q': 4, 'k': 5, 'p': 6,
                           'R': 7, 'N': 8, 'B': 9, 'Q': 10, 'K': 11, 'P': 12}
    state = []
    for letter in board_str:
        if ' ' not in letter and '\n' not in letter:
            state.append(pieces_dict[letter])
    print(state)
    return state


board = chess.Board()
print(board)
ai = agent.Agent(64)

a = get_state(board.__str__())
print(len(a))