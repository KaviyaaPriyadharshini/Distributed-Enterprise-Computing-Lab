import socket
import os
import uuid

# Simulate storage servers using a dictionary
storage_servers = {}

def split_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        fragment_size = len(data) // 2
        return data[:fragment_size], data[fragment_size:]

def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode()
    command, *args = request.split()

    if command == "UPLOAD":
        file_path = args[0]
        if os.path.exists(file_path):
            fragment1, fragment2 = split_file(file_path)
            file_id = str(uuid.uuid4())
            
            storage_servers[f"{file_id}_1"] = fragment1
            storage_servers[f"{file_id}_2"] = fragment2
            
            response = f"FILE_ID {file_id} FRAGMENTS {file_id}_1 {file_id}_2"
            client_socket.send(response.encode())
        else:
            client_socket.send("ERROR File not found".encode())

    elif command == "DOWNLOAD":
        file_id = args[0]
        fragments = [f"{file_id}_1", f"{file_id}_2"]
        full_file = b''

        for fragment in fragments:
            if fragment in storage_servers:
                full_file += storage_servers[fragment]
            else:
                client_socket.send("ERROR Fragment not found".encode())
                client_socket.close()
                return

        client_socket.send(full_file)

    client_socket.close()

def start_server(host='127.0.0.1', port=2000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client_connection(client_socket)

if __name__ == "__main__":
    start_server()
