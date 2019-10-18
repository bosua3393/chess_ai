import chess
import agent
from time import time


def get_state(board_str):
    pieces_dict = {'.': 0, 'r': 1, 'n': 2, 'b': 3, 'q': 4, 'k': 5, 'p': 6,
                           'R': 7, 'N': 8, 'B': 9, 'Q': 10, 'K': 11, 'P': 12}
    state = []
    for letter in board_str:
        if ' ' not in letter and '\n' not in letter:
            state.append(pieces_dict[letter])
    print(state)
    return state


def swap():
    pass


def main():
    teacher = agent.Agent(64)
    student = agent.Agent(64)
    while True:
        board = chess.Board()
        end = False
        while not end:
            a = get_state(board.__str__())
            if end:
                end = True
        if swap():
            teacher, student = student, teacher
            teacher.model.save(f'model/{time()}')


if __name__ == '__main__':
    main()
