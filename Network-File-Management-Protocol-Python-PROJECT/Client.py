

import os, sys
import socket

IP = socket.gethostbyname("localhost") #this will get the localhost IP address
PORT = 4458
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
CLIENT_DATA_PATH = "client_data"#this where the client data is stored

os.chdir(os.path.dirname(sys.argv[0]))


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.connect(ADDR)
    except:
        print("Server Is Not Ready \' Busy \' .")
        sys.exit()

    print("Welcome To 'Manage My Files' App!\n")
    print("Do You Want The Connection To Be:\n1 - Persistent\n2 - Non-Persistent:")

    try:
        while True:
            choose = input()

            if choose == "1":
                case = False
                commandList = "What Would You Like To Do ?\n1- List\n2- Download\n3- Upload\n4- Delete\n5- Make New Directory\n6- exit"
                LONG = 7
                print("Persistent Connection Opened Successfully \n")
                break

            elif choose == "2":
                case = True
                commandList = "What would you like to do ?\n1- list\n2- download\n3- upload\n4- delete\n5- make new directory\n"
                LONG = 6
                print("Non-Persistent Connection Opened Successfully \n")
                break
            else:
                print("ERROR- Wrong Choice")

        while True:

            print(commandList)

            while True:
                data = input("Enter Your Choice: ")
                try:
                    data = int(data)
                    if data in range(0, LONG):
                        cmd = data
                        break
                    else:
                        print("ERROR- Wrong Choice")
                except:
                    print("ERROR- Wrong Choice")

            if cmd == 1:
                list_path = input("Enter the path (/for current directory): ")
                client.send(("LIST@" + list_path).encode(FORMAT))
                info = client.recv(SIZE).decode(FORMAT)

                if info.startswith("100"):
                    print(f"\n{info[3:]}")
                elif info == "501":
                    print(f"\nThe Server Directory Is Empty")
                elif info == "502":
                    print(f"\nPath not found")




            elif cmd == 2:
                filename = input("Enter The Name Of The File: ")
                client.send(("DOWNLOAD@" + filename).encode(FORMAT))
                info = client.recv(SIZE).decode(FORMAT)

                if info == "100":
                    file_data = client.recv(SIZE).decode(FORMAT)

                    with open(f"{CLIENT_DATA_PATH}/{filename}", "w") as f:
                        f.write(file_data)

                    print("\nOperation Done Successfully.")
                else:
                    print(f"\nFile/Directory Path Not Found.")

            elif cmd == 3:
                file_name = input("Enter The Name Of The File: ")
                dest_path = input("Enter The Destination Path: ")

                try:
                    with open(f"{CLIENT_DATA_PATH}/{file_name}", "r") as f:
                        TEXT = f.read()

                    client.send(("UPLOAD@" + file_name + "@" + dest_path + "@" + TEXT).encode(FORMAT))
                    info = client.recv(SIZE).decode(FORMAT)
                    if info == "100":
                        print("\nOperation Done Successfully.")
                    elif info == "405":
                        print("\nUpload Failed.")

                except:
                    print("\nFile/Directory Not Found")

            elif cmd == 4:
                file_name = input("Enter File Name : ")
                client.send(("DELETE@" + file_name).encode(FORMAT))
                info = client.recv(SIZE).decode(FORMAT)
                if info == "501":
                    print("\nThe Server Directory Is Empty")
                elif info == "100":
                    print("\nFile Deleted Successfully")
                else:
                    print(f"\nFile/Directory Path Not Found.")


            elif cmd == 5:
                dir_path = input("Enter The Directory Name : ")
                client.send(("NEW DIRECTORY@" + dir_path).encode(FORMAT))
                info = client.recv(SIZE).decode(FORMAT)

                if info == "100":
                    print("Make Directory Successfully")
                else:
                    print("Fail To Make That Directory\n")

            elif cmd == 6:
                client.send("LOGOUT@".encode(FORMAT))
                print("\nConnection Closed Successfully \nDisconnected from the server..")
                client.close()
                break

            elif cmd == 0:
                client.send("HELP@".encode(FORMAT))
                info = client.recv(SIZE).decode(FORMAT)
                print(f"\n{info}")

            print("\n")

            if case == True:
                client.send("LOGOUT@".encode(FORMAT))
                print("\nConnection Closed Successfully \nDisconnected from the server..")
                client.close()
                break

    except:
        print("\nConnection Closed Successfully \nDisconnected from the server..")
        sys.exit()


if __name__ == "__main__":
    main()