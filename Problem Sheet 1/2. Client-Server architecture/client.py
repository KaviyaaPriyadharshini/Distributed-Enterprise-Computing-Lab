import socket

def upload_file(file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 2000))
        request = f"UPLOAD {file_path}"
        s.send(request.encode())
        response = s.recv(1024).decode()
        print("Server response:", response)
        return response.split()[1]  
    
def download_file(file_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 2000))
        request = f"DOWNLOAD {file_id}"
        s.send(request.encode())
        response = s.recv(1024)

        if response.startswith(b"ERROR"):
            print(response.decode())
        else:
            with open(f'downloaded_{file_id}.bin', 'wb') as f:
                f.write(response)
            print(f"File downloaded as downloaded_{file_id}.bin")

if __name__ == "__main__":
    file_id = upload_file('/home/cslinux/Desktop/file.txt')
    download_file(file_id)  
