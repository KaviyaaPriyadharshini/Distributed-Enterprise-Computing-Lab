import socket
import threading

# Define server host and port
HOST = '0.0.0.0'  # Allow connections from all IPs
PORT = 12345

# List to store connected client sockets
clients = []

# Broadcast message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:  # Do not send the message back to the sender
            try:
                client.send(message)
            except:
                # If the client is no longer reachable, remove it
                client.close()
                clients.remove(client)

# Handle communication with a single client
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if message:
                print(f"Received: {message.decode('utf-8')}")
                broadcast(message, client_socket)
        except:
            # Remove client on disconnect or error
            print("A client disconnected.")
            clients.remove(client_socket)
            client_socket.close()
            break

# Main function to set up the server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)  # Maximum 5 clients in the queue
    print(f"Server running on {HOST}:{PORT}...")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        # Start a new thread to handle this client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()
