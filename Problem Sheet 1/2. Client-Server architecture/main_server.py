import socket
import threading

# Constants
HOST = 'localhost'
PORT = 12345

class GameSession(threading.Thread):
    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def run(self):
        try:
            self.player1.sendall(b'You are Player 1 (X)\n')
            self.player2.sendall(b'You are Player 2 (O)\n')
            while True:
                if self.process_turn(self.player1, self.player2, 'X'):
                    break
                if self.process_turn(self.player2, self.player1, 'O'):
                    break
        except Exception as e:
            print(f"GameSession error: {e}")
        finally:
            self.player1.close()
            self.player2.close()

    def process_turn(self, current, opponent, token):
        try:
            current.sendall(b'Your move (row,col):\n')
            move = current.recv(1024).decode().strip()
            row, col = map(int, move.split(','))
            if self.board[row][col] != ' ':
                current.sendall(b'Invalid move. Try again.\n')
                return self.process_turn(current, opponent, token)
            self.board[row][col] = token

            if self.check_win(token):
                current.sendall(b'WIN\n')
                opponent.sendall(b'LOSE\n')
                return True
            elif self.is_draw():
                current.sendall(b'DRAW\n')
                opponent.sendall(b'DRAW\n')
                return True
            else:
                opponent.sendall(f'Opponent moved: {row},{col}\n'.encode())
                return False
        except Exception as e:
            print(f"Error processing turn: {e}")
            return True

    def check_win(self, token):
        for row in self.board:
            if all(cell == token for cell in row):
                return True
        for col in zip(*self.board):
            if all(cell == token for cell in col):
                return True
        if all(self.board[i][i] == token for i in range(3)) or \
           all(self.board[i][2 - i] == token for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)


def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server is running on {HOST}:{PORT}")

    try:
        while True:
            print("Waiting for players...")
            player1, addr1 = server.accept()
            print(f"Player 1 connected from {addr1}")
            player1.sendall(b'Waiting for another player...\n')

            player2, addr2 = server.accept()
            print(f"Player 2 connected from {addr2}")
            player1.sendall(b'Starting the game...\n')
            player2.sendall(b'Starting the game...\n')

            session = GameSession(player1, player2)
            session.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server.close()


if __name__ == '__main__':
    main()
