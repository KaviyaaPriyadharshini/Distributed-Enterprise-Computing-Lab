#client.py
import ftplib
import os

HOSTNAME = "127.0.0.1"  
USERNAME = "user"      
PASSWORD = "pwd"        
PORT = 1025            

ftp_server = ftplib.FTP()
ftp_server.connect(HOSTNAME, PORT)  
ftp_server.login(USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

directory_path = "/home/cslinux/Desktop/DEC Lab/Client"
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):  
        with open(file_path, "rb") as file:
            ftp_server.storbinary(f"STOR {filename}", file)  
            print(f"Uploaded: {filename}")  
ftp_server.dir()
ftp_server.quit()
