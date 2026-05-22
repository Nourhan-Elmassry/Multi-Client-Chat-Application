# Video Narration Script

Use this script while presenting the Gamma slides and recording the live demo.

## Slide 1 - Title

Hello doctor. My project is called Multi-Client Chat Application. It is a Computer Networks project implemented in Python using socket programming and threading.

The idea is to allow more than one client to connect to the same server and exchange messages in real time.

## Slide 2 - Project Objective

The main objective of this project is to build a simple real-time chat system.

The system has one central server and multiple clients. Each client can send a message, and the server broadcasts that message to the other connected clients.

This project focuses on TCP sockets, multiple client connections, message broadcasting, and safe disconnection.

## Slide 3 - Technologies Used

The project uses Python 3.

I used the built-in `socket` library to create the network connection between the server and the clients.

I also used the built-in `threading` library so the server can handle multiple clients at the same time.

The program runs in the terminal, and it does not need any external libraries.

## Slide 4 - System Architecture

The application uses a client-server architecture.

The server runs on the local address `127.0.0.1` and port `5000`.

Clients do not communicate directly with each other. Instead, each client connects to the server. When one client sends a message, the server receives it and forwards it to the other connected clients.

This makes the server the central point that manages communication.

## Slide 5 - Server Responsibilities

Now I will explain the server file, which is `server.py`.

The server creates a TCP socket, binds it to the host and port, and starts listening for clients.

When a client connects, the server accepts the connection and creates a new thread for that client.

The server also stores connected clients in a list, broadcasts messages, and removes clients when they leave.

## Slide 6 - Client Responsibilities

The second main file is `client.py`.

The client connects to the server, asks the user to enter a username, and then allows the user to send messages.

The client also starts a separate receiving thread. This is important because the user can receive messages while typing another message.

The client can leave the chat by typing `/exit`.

## Slide 7 - Threading Concept

Threading is one of the most important parts of this project.

Without threading, the server might wait for one client and block other clients.

In this project, every connected client gets its own thread on the server. This allows the server to receive messages from multiple clients at the same time.

The client also uses a thread to receive messages from the server in the background.

## Slide 8 - Broadcasting Logic

The broadcasting logic works like this.

First, a client sends a message to the server. Then the server receives the message and calls the broadcast function.

The broadcast function sends the message to all connected clients except the sender.

For example, if Ahmad sends "Hello Sara", Sara receives "Ahmad: Hello Sara". Ahmad does not receive his own message again.

## Slide 9 - Graceful Exit

The project also handles graceful exit.

When a client types `/exit`, the client closes its socket connection.

The server detects that this client disconnected, removes the client from the active clients list, and keeps running normally.

This is important because one client leaving should not crash the whole server.

## Slide 10 - Live Demo and Conclusion

Now I will run the project.

First, I will start the server using `py server.py` on Windows. If Python is configured in PATH, the command can also be `python server.py`.

Now the server is waiting for clients.

Next, I will open the first client using `py client.py` and enter the username Ahmad.

Then I will open a second client and enter the username Sara.

Now both clients are connected to the same server.

I will send a message from Ahmad: "Hello Sara".

Sara receives the message as "Ahmad: Hello Sara".

Now I will reply from Sara: "Hi Ahmad".

Ahmad receives the message as "Sara: Hi Ahmad".

Finally, I will type `/exit` from Sara's client.

Sara leaves the chat, but the server continues running. This shows that the graceful exit requirement works correctly.

In conclusion, this project demonstrates the main requirements of the assignment: socket programming, multiple clients, threading, message broadcasting, and safe client disconnection.
