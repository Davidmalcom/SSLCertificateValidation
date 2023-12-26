import ssl
import socket
class SSLServerSocket:
    def __init__(self, certfile, keyfile, bind_address, port):
        self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.context.load_cert_chain(certfile, keyfile)
        self.bind_address = bind_address
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            print(f"Binding to {self.bind_address}:{self.port}")
            server_socket.bind((self.bind_address, self.port))
            server_socket.listen(5)
            print(f"Server is listening on {self.bind_address}:{self.port}")

            with self.context.wrap_socket(server_socket, server_side=True) as secure_socket:
                conn, addr = secure_socket.accept()
                print(f"Connection established from {addr}")
                data = conn.recv(1024).decode('utf-8')
                is_valid_license = self.check_license(data)  # Replace this with your license validation logic

                if is_valid_license:
                    conn.sendall(b"License is valid")
                else:
                    conn.sendall(b"Invalid license")
                conn.close()

    def check_license(self, license_key):
        valid_license_key = "VALID_LICENSE_KEY"
        return license_key == valid_license_key


if __name__ == "__main__":
    server = SSLServerSocket('server.crt', 'server.key', 'localhost', 8888)
    server.start_server()
