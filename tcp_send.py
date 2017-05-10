import socket
import sys
import time


HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
def sendnum(target=100):
    count = 0
    for i in range(target):
        data = str(count)
        count += 1
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        time.sleep(0.1)


if __name__ == "__main__":
    sendnum()
