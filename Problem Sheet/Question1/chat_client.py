import socket
import threading

# Define server host and port
SERVER_HOST = '127.0.0.1'  # Replace with the server's IP address
SERVER_PORT = 12345

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection lost.")
            client_socket.close()
            break

# Main function to set up the client
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_HOST, SERVER_PORT))
    except:
        print("Unable to connect to the server.")
        return

    print("Connected to the chat server.")
    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    # Start a thread to listen for incoming messages
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    # Main loop to send messages
    while True:
        message = input("")
        if message.lower() == 'exit':
            client.close()
            break
        else:
            client.send(f"{username}: {message}".encode('utf-8'))

if __name__ == "__main__":
    main()
