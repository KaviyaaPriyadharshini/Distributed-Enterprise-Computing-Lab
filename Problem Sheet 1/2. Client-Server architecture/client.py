import socket

HOST = 'localhost'
PORT = 12345

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            print("Connected to the server.")

            while True:
                server_message = client.recv(1024).decode()
                print(server_message.strip())
                if server_message.startswith('Your move'):
                    move = input("Enter your move (row,col): ")
                    client.sendall(move.encode())
                elif server_message in ['WIN', 'LOSE', 'DRAW']:
                    print(f"Game over: {server_message}")
                    break
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
