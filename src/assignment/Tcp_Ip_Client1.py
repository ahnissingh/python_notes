import socket
def tcp_client():
    server_address = '127.0.0.1'
    server_port = 65423

    # Create the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        print(f'Connecting to {server_address} at port {server_port}')
        client_socket.connect((server_address, server_port))

        # Send message to the server
        msg = "Hello Server"
        print(f"Sending message: {msg}")
        client_socket.sendall(msg.encode('utf-8'))

        # Receive response from the server
        data = client_socket.recv(1024)
        print(f'Received from server: {data.decode("utf-8")}')

    except socket.error as e:
        print(f'Error: {e}')
    finally:
        # Close the connection
        print('Closing connection.')
        client_socket.close()


if __name__ == '__main__':
    tcp_client()
