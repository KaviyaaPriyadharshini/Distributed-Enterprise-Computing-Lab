# client.py
import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 5004
FILE_PATH = 'C:\DEC Lab\File.txt'

def upload_file():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
    except Exception as error:
        print(f"Connection failed: {error}")
        return

    try:
        client_socket.send(FILE_PATH.encode())
        server_response = client_socket.recv(1024)
        print(server_response.decode())
    except Exception as error:
        print(f"Error during upload: {error}")
    finally:
        client_socket.close()

upload_file()
