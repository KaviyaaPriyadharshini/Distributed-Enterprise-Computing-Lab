# server.py
import socket
import os
import threading

MAIN_SERVER_HOST = 'localhost'
MAIN_SERVER_PORT = 5004
STORAGE_SERVERS = [('localhost', 5001), ('localhost', 5002)]
FRAGMENT_BUFFER = 1024

def process_storage_connection(conn):
    while True:
        data = conn.recv(FRAGMENT_BUFFER)
        if not data:
            break
        with open('storage_log.txt', 'ab') as storage_file:
            storage_file.write(data)
    conn.close()

def initialize_storage_server(port):
    storage_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    storage_socket.bind(('localhost', port))
    storage_socket.listen(5)
    print(f'Storage server active on port {port}...')
    while True:
        conn, addr = storage_socket.accept()
        print(f'Connected to {addr}')
        process_storage_connection(conn)

def main_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((MAIN_SERVER_HOST, MAIN_SERVER_PORT))
    server_socket.listen(5)
    print('Main server operational...')

    while True:
        client_conn, client_addr = server_socket.accept()
        print(f'Client linked from {client_addr}')
        
        file_location = client_conn.recv(FRAGMENT_BUFFER).decode()
        if not os.path.exists(file_location):
            client_conn.send(b'Error: File not available.')
            client_conn.close()
            continue

        segment_index = 0
        with open(file_location, 'rb') as file_segment:
            while True:
                fragment = file_segment.read(FRAGMENT_BUFFER)
                if not fragment:
                    break

                server_index = segment_index % len(STORAGE_SERVERS)
                target_host, target_port = STORAGE_SERVERS[server_index]

                try:
                    storage_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    storage_conn.connect((target_host, target_port))
                    storage_conn.sendall(fragment)
                    storage_conn.close()
                except Exception as error:
                    print(f"Transmission error to {target_host}:{target_port} - {error}")

                segment_index += 1

        client_conn.send(b'Upload finalized.')
        client_conn.close()

for port in range(5001, 5003):
    threading.Thread(target=initialize_storage_server, args=(port,), daemon=True).start()

main_server()
