import socketserver
import threading

class MyTCPHandler(socketserver.BaseRequestHandler):

    def putter(self, value):
        for queue in self.server.queues:
            queue.put(value)

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        value = int(self.data)
        self.putter(value = value)
        # just send back the same data, but upper-cased
        self.request.sendall(("200").encode())

def OpenRecv(queues):
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.queues = queues
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
