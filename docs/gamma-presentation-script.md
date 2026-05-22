# Gamma Presentation Script

Paste the following content into Gamma to generate the presentation.

## Gamma Prompt

Create a clean 10-slide presentation for a Computer Networks course project titled "Multi-Client Chat Application". The project is implemented in Python using sockets and threading. The presentation should explain the objective, architecture, server code, client code, threading, broadcasting, graceful exit, and a short live demo plan. Use simple academic English, clear diagrams, and concise bullet points.

## Slide 1 - Title

Multi-Client Chat Application  
Computer Networks Project  
Built with Python Socket Programming and Threading

## Slide 2 - Project Objective

The objective is to build a real-time chat system where multiple clients can communicate through one central server.

Main goals:

- Use TCP sockets for network communication.
- Allow multiple clients to connect at the same time.
- Broadcast messages from one client to all other clients.
- Handle client disconnection without crashing the server.

## Slide 3 - Technologies Used

- Python 3
- socket library for TCP communication
- threading library for concurrency
- Terminal-based user interface
- UTF-8 encoding for text messages

No external libraries are required.

## Slide 4 - System Architecture

The application follows a client-server architecture.

- The server listens on `127.0.0.1:5000`.
- Each client connects to the server.
- The server creates a separate thread for every client.
- Messages are received by the server and then forwarded to other clients.

Suggested diagram:

Client Ahmad -> Server -> Client Sara  
Client Sara -> Server -> Client Ahmad

## Slide 5 - Server Responsibilities

The server file is `server.py`.

It is responsible for:

- Creating the TCP socket.
- Binding the socket to host and port.
- Listening for incoming connections.
- Accepting clients.
- Starting a new thread for each client.
- Broadcasting messages.
- Removing disconnected clients safely.

## Slide 6 - Client Responsibilities

The client file is `client.py`.

It is responsible for:

- Connecting to the server.
- Asking the user for a username.
- Sending messages typed by the user.
- Receiving messages from the server.
- Leaving the chat using `/exit`.

The client uses a receiving thread so messages can arrive while the user is typing.

## Slide 7 - Threading Concept

Threading is used to prevent blocking.

On the server:

- One main loop accepts new clients.
- Each connected client is handled by a separate thread.

On the client:

- The main thread sends messages.
- A background thread receives messages.

This allows real-time communication between multiple users.

## Slide 8 - Broadcasting Logic

When a client sends a message:

1. The server receives the message.
2. The server identifies the sender.
3. The server sends the message to all other connected clients.
4. The sender does not receive the same message back.

Example:

Ahmad sends: `Hello Sara`  
Sara receives: `Ahmad: Hello Sara`

## Slide 9 - Graceful Exit

Clients can leave the chat by typing:

`/exit`

When this happens:

- The client closes its socket.
- The server detects the disconnection.
- The server removes the client from the active clients list.
- The server keeps running for other connected clients.

This satisfies the graceful exit requirement.

## Slide 10 - Demo and Conclusion

Demo steps:

1. Run `py server.py` on Windows, or `python server.py` if Python is configured in PATH.
2. Run two clients using `py client.py`.
3. Connect as Ahmad and Sara.
4. Send messages between both clients.
5. Exit one client using `/exit`.
6. Show that the server still works.

Conclusion:

This project demonstrates TCP socket programming, multi-client handling, threading, broadcasting, and safe disconnection in a simple real-time chat application.
