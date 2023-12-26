import socket
import ssl

def connect_to_server():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection(('localhost', 8888)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname='localhost') as secure_socket:
            license_key = "VALID_LICENSE_KEY"  # Replace with your actual license key
            secure_socket.sendall(license_key.encode('utf-8'))
            response = secure_socket.recv(1024)
            print(response.decode('utf-8'))

if __name__ == "__main__":
    connect_to_server()
