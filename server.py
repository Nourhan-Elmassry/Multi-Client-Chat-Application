import socket
import threading


HOST = "127.0.0.1"
PORT = 5000
ENCODING = "utf-8"


clients = []
clients_lock = threading.Lock()
log_lock = threading.Lock()


def log(message):
    """Print server messages without mixing output from multiple threads."""
    with log_lock:
        print(message, flush=True)


def remove_client(client):
    """Remove a disconnected client from the active clients list."""
    with clients_lock:
        if client not in clients:
            return False, len(clients)

        clients.remove(client)
        active_clients = len(clients)

    try:
        client["socket"].close()
    except OSError:
        pass

    return True, active_clients


def broadcast(message, sender_socket=None):
    """Send a message to all connected clients except the sender."""
    disconnected_clients = []

    with clients_lock:
        recipients = [
            client for client in clients if client["socket"] != sender_socket
        ]

    for client in recipients:
        client_socket = client["socket"]

        try:
            client_socket.sendall(f"{message}\n".encode(ENCODING))
        except (ConnectionResetError, BrokenPipeError, OSError):
            disconnected_clients.append(client)

    for client in disconnected_clients:
        removed, active_clients = remove_client(client)
        if removed:
            log(f"[LEFT] {client['username']} left the chat.")
            log(f"[ACTIVE CLIENTS] {active_clients}")


def handle_client(client_socket, client_address):
    username = "Unknown"
    client = None
    client_file = None

    try:
        client_file = client_socket.makefile("r", encoding=ENCODING)
        username = client_file.readline().strip()
        if not username:
            username = f"{client_address[0]}:{client_address[1]}"

        client = {"socket": client_socket, "address": client_address, "username": username}

        with clients_lock:
            clients.append(client)
            active_clients = len(clients)

        log(f"[NEW CONNECTION] {username} connected from {client_address}")
        log(f"[ACTIVE CLIENTS] {active_clients}")
        broadcast(f"[SERVER] {username} joined the chat.", client_socket)

        while True:
            message = client_file.readline()

            if not message:
                break

            decoded_message = message.strip()

            if not decoded_message:
                continue

            log(f"[MESSAGE] {username}: {decoded_message}")
            broadcast(f"{username}: {decoded_message}", client_socket)

    except (ConnectionResetError, BrokenPipeError):
        log(f"[DISCONNECTED] {username} disconnected unexpectedly.")
    except OSError as error:
        log(f"[ERROR] Connection problem with {username}: {error}")
    finally:
        if client_file is not None:
            client_file.close()

        if client is not None:
            removed, active_clients = remove_client(client)

            if removed:
                log(f"[LEFT] {username} left the chat.")
                log(f"[ACTIVE CLIENTS] {active_clients}")
                broadcast(f"[SERVER] {username} left the chat.", client_socket)
        else:
            try:
                client_socket.close()
            except OSError:
                pass


def start_server():
    # Socket creation and binding.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    log(f"[STARTED] Server is running on {HOST}:{PORT}")
    log("[WAITING] Waiting for clients to connect...")

    try:
        while True:
            # Accept each client, then handle it in a separate thread.
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address),
                daemon=True,
            )
            thread.start()
    except KeyboardInterrupt:
        log("\n[SHUTDOWN] Server is shutting down...")
    finally:
        with clients_lock:
            for client in clients:
                try:
                    client["socket"].close()
                except OSError:
                    pass
            clients.clear()

        server_socket.close()


if __name__ == "__main__":
    start_server()
