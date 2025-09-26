from socket import *
import threading

def handle_client(conn, cliente):
    """Função para lidar com a comunicação de cada cliente em sua própria thread."""
    print('Conectado por:', cliente)
    while True:
        try:
            recvMsg = conn.recv(1024)
            if recvMsg == b'\x18' or not recvMsg:
                break
            print(cliente, recvMsg.decode())
        except ConnectionResetError:
            break
    print('Finalizando conexão do cliente', cliente)
    conn.close()

meuHost = ''
minhaPorta = 5001
sockobj = socket(AF_INET, SOCK_STREAM)
orig = (meuHost, minhaPorta)
sockobj.bind(orig)
sockobj.listen(1)

# Loop principal agora apenas aceita conexões e dispara threads
while True:
    conn, cliente = sockobj.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, cliente))
    client_thread.start()