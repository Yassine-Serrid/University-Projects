#Yassin Serrid 2181156439
#Abdulrahman Mohammed

import os, sys
import socket



IP = socket.gethostbyname("localhost")
PORT = 4458
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

os.chdir(os.path.dirname(sys.argv[0]))


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected..")

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "LIST":
            list_path = data[1]
            try:
                files = os.listdir(f"{SERVER_DATA_PATH}{list_path}")
                if len(files) == 0:
                    send_data = "501"
                else:
                    send_data = "100\n"
                    send_data += "\n".join(f for f in files)
            except:
                send_data = "502"
            conn.send(send_data.encode(FORMAT))

        elif cmd == "DOWNLOAD":
            file_name = data[1]
            find_it = os.path.exists(f"{SERVER_DATA_PATH}/{file_name}")
            if find_it:
                conn.send('100'.encode(FORMAT))

                with open(f"{SERVER_DATA_PATH}/{file_name}", "r") as f:
                    text = f.read()

                conn.send(text.encode(FORMAT))

            else:
                conn.send("502".encode(FORMAT))

        elif cmd == "UPLOAD":
            try:
                name, dest, text = data[1], data[2], data[3]
                if dest.startswith("/"):
                    pass
                else:
                    dest = "/" + dest
                if dest.endswith("/"):
                    pass
                else:
                    dest = dest + "/"

                with open(f"{SERVER_DATA_PATH}{dest}{name}", "w") as f:
                    f.write(text)

                conn.send("100".encode(FORMAT))
            except:
                conn.send("405".encode(FORMAT))

        elif cmd == "DELETE":
            filename = data[1]
            if "/" in filename:
                FileName = filename.split("/")[-1]
                bath = os.path.dirname(filename)
                if bath.startswith("/"):
                    files = os.listdir(SERVER_DATA_PATH + bath)
                else:
                    bath = "/" + bath
                    files = os.listdir(SERVER_DATA_PATH + "/" + bath)
            else:
                FileName = filename
                bath = ""
                files = os.listdir(SERVER_DATA_PATH)

            if len(files) == 0:
                send_data = "501"
            else:
                if FileName in files:
                    if not bath:
                        os.remove(f"{SERVER_DATA_PATH}/{FileName}")
                        send_data = "100"
                    else:
                        os.remove (f"{SERVER_DATA_PATH}{bath}/{FileName}")
                else:
                    send_data = "502"

            conn.send(send_data.encode(FORMAT))

        elif cmd == "NEW DIRECTORY":
            dir_path = data[1]
            if not dir_path.startswith("/"):
                dir_path = "/" + dir_path

            os.mkdir(f"{SERVER_DATA_PATH}{dir_path}")
            if os.path.exists(f"{SERVER_DATA_PATH}{dir_path}"):
                send_data = "100"
            else:
                send_data = "404"

            conn.send(send_data.encode(FORMAT))

        elif cmd == "LOGOUT":
            break

        elif cmd == "HELP":
            data = ""
            data += "LIST: List all the files from the server.\n"
            data += "UPLOAD <path>: Upload a file to the server.\n"
            data += "DELETE <filename>: Delete a file from the server.\n"
            data += "LOGOUT: Disconnect from the server.\n"
            data += "HELP: List all the commands.."

            conn.send(data.encode(FORMAT))

    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()


def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}.")

    conn, addr = server.accept()
    print("[ACTIVE CONNECTIONS]")
    handle_client(conn, addr)


if __name__ == "__main__":
    main()