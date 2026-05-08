# Multi-Client Chat Application

## Project Overview

This project is a simple real-time chat application built with Python.

The main idea is to have one server that can accept multiple clients at the same time. Each client can send messages, and the server broadcasts these messages to the other connected clients.

The project uses Python's built-in `socket` library for network communication and the `threading` library to handle more than one client at the same time.

This project is designed to be simple and suitable for a Computer Networks course project. It does not use a GUI, database, external libraries, or advanced frameworks.

## Objective

The objective of this project is to demonstrate how a real-time multi-client chat system works using basic networking concepts.

The project focuses on:

- Creating a TCP socket server.
- Connecting multiple clients to the same server.
- Handling every client using a separate thread.
- Sending messages from one client to other clients.
- Handling client exit or disconnection without stopping the server.

## Technologies Used

- Python 3
- `socket` library
- `threading` library
- Terminal / Command Line
- UTF-8 encoding

## Main Features

- The server can handle multiple clients at the same time.
- Each connected client has its own thread on the server.
- The client has a simple terminal interface.
- Each client enters a username before joining the chat.
- Messages are broadcasted to the other connected clients.
- The sender does not receive the same message back.
- Clients can leave using the `/exit` command.
- The server keeps running even if one client disconnects.
- The application supports both English and Arabic text using UTF-8.

## Project Files

```text
server.py   - starts the chat server and handles all connected clients
client.py   - connects to the server and lets the user send and receive messages
README.md   - contains the project explanation and demo steps
```

## Network Configuration

Both `server.py` and `client.py` use the same host and port:

```python
HOST = "127.0.0.1"
PORT = 5000
```

`127.0.0.1` means the application runs locally on the same computer. This is useful for testing the project and recording the demo video.

## How the Server Works

The server starts by creating a TCP socket.

After that, it binds the socket to the host and port, then starts listening for client connections.

When a new client connects, the server accepts the connection and starts a new thread for that client.

Each thread is responsible for receiving messages from one client. This allows the server to keep listening to all clients at the same time.

The server also stores all connected clients in a list. This list is used when the server needs to broadcast a message.

## How the Client Works

The client connects to the server using the same host and port.

When the client starts, it asks the user to enter a username. This username is sent to the server and used when sending messages.

The client uses a separate receiving thread to listen for incoming messages from the server.

At the same time, the main part of the client program allows the user to type and send messages.

This means the user can receive messages while typing, which makes the chat feel real-time.

## How Broadcasting Works

When a client sends a message, the server receives it first.

Then the server uses the `broadcast` function to send this message to all other connected clients.

The message is not sent back to the same client who wrote it.

For example:

```text
Ahmad sends: Hello Sara
```

Sara receives:

```text
Ahmad: Hello Sara
```

This shows that the server is responsible for distributing messages between clients.

## How Threading is Used

Threading is important in this project because the server must handle more than one client at the same time.

Without threading, the server might wait for one client and block the others.

In this project, every client connection gets a separate thread. So if Ahmad sends a message and Sara is also connected, the server can still handle both clients independently.

The client also uses a receiving thread, so it can receive messages from the server while the user is typing.

## How Graceful Exit Works

The client can leave the chat by typing:

```text
/exit
```

When a client exits, the connection is closed.

The server detects this disconnection, removes the client from the active clients list, and keeps running normally.

This is important because one disconnected client should not crash the whole server.

## How to Run

First, run the server:

```bash
python server.py
```

Then open two different terminal windows and run the client in each one:

```bash
python client.py
```

Use different usernames, for example:

```text
Ahmad
Sara
```

To leave the chat, type:

```text
/exit
```

## Practical Demo with Ahmad and Sara

1. Run the server:

```bash
python server.py
```

2. Open the first client and enter:

```text
Ahmad
```

3. Open the second client and enter:

```text
Sara
```

4. From Ahmad's terminal, send:

```text
Hello Sara
```

5. Sara should receive:

```text
Ahmad: Hello Sara
```

6. From Sara's terminal, send:

```text
Hi Ahmad
```

7. Ahmad should receive:

```text
Sara: Hi Ahmad
```

8. From Sara's terminal, type:

```text
/exit
```

9. The server should stay running, and Ahmad can remain connected.

## Video Explanation Script

Hello doctor, this is my Multi-Client Chat Application project.

The goal of this project is to build a simple real-time chat system using Python. The project uses the `socket` library for network communication and the `threading` library to allow multiple clients to connect at the same time.

The project contains two main files. The first file is `server.py`, which starts the server, accepts client connections, creates a thread for each client, and broadcasts messages. The second file is `client.py`, which connects to the server and allows the user to send and receive messages from the terminal.

First, I will run the server using `python server.py`. The server is now running on `127.0.0.1` and port `5000`, and it is waiting for clients.

Now I will open two clients. In the first client, I will use the username `Ahmad`. In the second client, I will use the username `Sara`.

At this point, both clients are connected to the same server. The server created a separate thread for each client, so it can handle both clients at the same time.

Now Ahmad will send a message: `Hello Sara`.

Sara receives the message as `Ahmad: Hello Sara`. This means the server received the message from Ahmad and broadcasted it to Sara.

Now Sara will reply with `Hi Ahmad`.

Ahmad receives the message as `Sara: Hi Ahmad`.

An important point is that the message is sent to the other clients only. The sender does not receive the same message back.

Finally, I will test the exit feature. Sara types `/exit` to leave the chat. The server detects that Sara disconnected, removes her from the clients list, and continues running normally.

This project demonstrates the main networking requirements: socket programming, multiple clients, threading, broadcasting, and safe disconnection handling.
