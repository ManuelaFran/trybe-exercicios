# Agora vamos para a camada de transporte. Crie um servidor TCP usando o
# módulo socketserver que já vem embutido com o Python. Nosso servidor TCP
# deverá:
# Responder com um “Olá, client”, logo quando estabelecer uma conexão.
# Imprimir no console todo dado recebido.
# Responder com os dados recebidos (como um eco).
# Utilizar a porta 8085.

from socketserver import TCPServer, StreamRequestHandler

ADDRESS = "", 8085


class EchoHandler(StreamRequestHandler):
    def handle(self):
        self.wfile.write(b"Hello, World!\n")
        for line in self.rfile:
            self.wfile.write(line)
            print(line.decode('ascii').strip())


if __name__ == "__main__":
    with TCPServer(ADDRESS, EchoHandler) as server:
        server.serve_forever()
