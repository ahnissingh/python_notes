import socket
import threading


class ChatClient:
    def __init__(self, server_address, server_port):
        # Server address and port
        self.server_address = server_address
        self.server_port = server_port
        # Create a TCP socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        """Connect to the chat server."""
        try:
            # Connect to the server
            self.client_socket.connect((self.server_address, self.server_port))
            self.connected = True
            print(f"Connected to the server at {self.server_address}:{self.server_port}")
        except ConnectionRefusedError:
            print("Failed to connect to the server. Please ensure the server is running.")
            return

        # Start the send and receive threads
        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.send_messages()

    def receive_messages(self):
        """Receive messages from the server."""
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n[Server] {message}")
                else:
                    # Server has closed the connection
                    print("Connection closed by the server.")
                    self.connected = False
                    break
            except ConnectionResetError:
                print("Connection reset by the server.")
                self.connected = False
                break
            except Exception as e:
                print(f"Error receiving message: {e}")
                self.connected = False
                break
        self.disconnect()

    def send_messages(self):
        """Send messages to the server."""
        while self.connected:
            try:
                message = input("You: ")
                if message.lower() == "exit":
                    # User wants to disconnect
                    self.connected = False
                    break
                # Send the message to the server
                self.client_socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message: {e}")
                self.connected = False
                break
        self.disconnect()

    def disconnect(self):
        """Close the connection to the server."""
        if self.connected:
            self.client_socket.close()
            self.connected = False
            print("Disconnected from the server.")


# Run the chat client
if __name__ == "__main__":
    # Define server details (localhost and port)
    SERVER_ADDRESS = "127.0.0.1"  # Localhost for testing
    SERVER_PORT = 65432  # Must match the server's port

    # Create the client and connect to the server
    client = ChatClient(SERVER_ADDRESS, SERVER_PORT)
    client.connect()
