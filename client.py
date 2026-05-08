import socket
import threading


HOST = "127.0.0.1"
PORT = 5000
ENCODING = "utf-8"
EXIT_COMMAND = "/exit"


def receive_messages(client_socket, stop_event):
    """Receive messages from the server in a separate thread."""
    try:
        with client_socket.makefile("r", encoding=ENCODING) as server_file:
            while not stop_event.is_set():
                message = server_file.readline()

                if not message:
                    print("\n[INFO] Server closed the connection.")
                    stop_event.set()
                    break

                print(f"\n{message.strip()}")
    except (ConnectionResetError, ConnectionAbortedError):
        print("\n[INFO] Connection to the server was lost.")
        stop_event.set()
    except OSError:
        stop_event.set()


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stop_event = threading.Event()

    try:
        # Connect to the socket server.
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to the server. Make sure server.py is running.")
        return

    try:
        username = input("Enter your username: ").strip()
    except EOFError:
        print("[INFO] No username entered. Closing client.")
        client_socket.close()
        return

    if not username:
        username = "Anonymous"

    try:
        client_socket.sendall(f"{username}\n".encode(ENCODING))
    except (ConnectionResetError, BrokenPipeError, OSError):
        print("[ERROR] Could not send username. Connection is closed.")
        client_socket.close()
        return

    print("\nConnected to the chat server.")
    print(f"Type your message and press Enter. Type {EXIT_COMMAND} to leave.\n")

    # Threading allows receiving messages while the user is typing.
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client_socket, stop_event),
        daemon=True,
    )
    receive_thread.start()

    try:
        while not stop_event.is_set():
            try:
                message = input()
            except EOFError:
                print("\n[INFO] Input closed. Leaving the chat.")
                stop_event.set()
                break

            if message.strip() == EXIT_COMMAND:
                print("[INFO] You left the chat.")
                stop_event.set()
                break

            if not message.strip():
                continue

            try:
                client_socket.sendall(f"{message}\n".encode(ENCODING))
            except (ConnectionResetError, BrokenPipeError, OSError):
                print("[INFO] Could not send message. Connection is closed.")
                stop_event.set()
                break
    except KeyboardInterrupt:
        print("\n[INFO] You left the chat.")
        stop_event.set()
    finally:
        try:
            client_socket.close()
        except OSError:
            pass


if __name__ == "__main__":
    start_client()
