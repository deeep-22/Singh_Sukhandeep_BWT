import socket
from app import trasforma

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:


    server.bind(("127.0.0.1", 5000))

    server.listen()

    print("Server in ascolto...")
    print("Socket di ascolto:", server.getsockname())

    conn, addr = server.accept()

    with conn:
        print("Client connesso:", addr)

        print("Socket di connessione:", conn.getsockname())

    
        messaggio = conn.recv(1024).decode()
        trasformato = trasforma(messaggio)
        

        conn.sendall(trasformato.encode())