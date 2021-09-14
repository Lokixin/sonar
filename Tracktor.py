""" This script contains the Tracktor class. It would read tracktor boradcasted messages.

This class is mainly a TCP Server listening to the tracktor broadcast. It would read
the song information provided by the Tracktor software ( hopefully :D ). 
"""

import socketserver

class Tracktor(socketserver.BaseRequestHandler):

    def __init__(self):
        super().__init__()

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), Tracktor) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()