import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                print("[SERVER] Connection closed.")
                break
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")
            break

def send_messages(client_socket):
    while True:
        message = input()
        if message.lower() == 'exit':
            print("[INFO] Disconnecting from the chat.")
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print("[INFO] Connected to the server.")
    except Exception as e:
        print(f"[ERROR] Could not connect to server: {e}")
        return

    # Set username
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)

if __name__ == "__main__":
    host = input("Enter server IP address: ")
    port = 1026
    start_client(host, port)
