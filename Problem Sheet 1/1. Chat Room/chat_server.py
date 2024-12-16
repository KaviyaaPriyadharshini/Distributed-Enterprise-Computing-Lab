import socket
import threading

clients = {}
clients_lock = threading.Lock()

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    client_socket.send("Welcome to the chat room!".encode('utf-8'))
    
    username = client_socket.recv(1024).decode('utf-8')
    with clients_lock:
        clients[client_socket] = username
    print(f"[USERNAME SET] {username} has joined the chat.")

    broadcast(f"[{username}] has joined the chat!", client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{username}] {message}")
                broadcast(f"[{username}] {message}", client_socket)
            else:
                break
        except Exception as e:
            print(f"[ERROR] {username} disconnected unexpectedly: {e}")
            break

    with clients_lock:
        del clients[client_socket]
    print(f"[DISCONNECTED] {username} disconnected.")
    broadcast(f"[{username}] has left the chat.", client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    with clients_lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"[ERROR] Could not send message to a client: {e}")

def start_server(host='0.0.0.0', port=1026):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"[STARTING SERVER] Server started on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    start_server()
