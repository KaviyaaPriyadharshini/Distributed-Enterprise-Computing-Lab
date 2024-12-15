import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 12345))
    except Exception as e:
        print(f"Connection error: {e}")
        return

    try:
        while True:
            message = client_socket.recv(1024).decode()
            print(message)  

            if "wins" in message or "draw" in message:
                break  

            if "turn" in message:
                move = input("Enter your move (0-8): ")
                while not (move.isdigit() and 0 <= int(move) < 9):
                    print("Invalid input. Please enter a number between 0 and 8.")
                    move = input("Enter your move (0-8): ")
                client_socket.sendall(move.encode())  
    except Exception as e:
        print(f"Error during communication: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
