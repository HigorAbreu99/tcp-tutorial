from socket import *
import threading

meuHost = ''
minhaPorta = 5001

# 1. Lista para armazenar as conexões dos clientes e um Lock para segurança
clientes_conectados = []
lock = threading.Lock()

def broadcast(mensagem, remetente_conn):
    """
    Envia uma mensagem para todos os clientes conectados, exceto para quem a enviou.
    """
    with lock: # Adquire o lock para poder iterar na lista com segurança
        for cliente_conn in clientes_conectados:
            # Não envia a mensagem de volta para o remetente
            if cliente_conn != remetente_conn:
                try:
                    cliente_conn.send(mensagem)
                except:
                    # Se ocorrer um erro (ex: cliente desconectado), fecha e remove
                    cliente_conn.close()
                    clientes_conectados.remove(cliente_conn)

def handle_client(conn, cliente_addr):
    """
    Função para lidar com a comunicação de cada cliente em sua própria thread.
    """
    print('Conectado por:', cliente_addr)
    
    # Adiciona a nova conexão à lista de forma segura
    with lock:
        clientes_conectados.append(conn)

    try:
        while True:
            recvMsg = conn.recv(1024)
            if recvMsg == b'\x18' or not recvMsg:
                break
            
            # Monta a mensagem para retransmissão e chama o broadcast
            mensagem_formatada = f"<{cliente_addr[0]}:{cliente_addr[1]}>: ".encode() + recvMsg
            print(f"Mensagem recebida de {cliente_addr}: {recvMsg.decode()}")
            broadcast(mensagem_formatada, conn)
            
    finally:
        # Garante que o cliente seja removido da lista ao se desconectar
        print('Finalizando conexão do cliente', cliente_addr)
        with lock:
            if conn in clientes_conectados:
                clientes_conectados.remove(conn)
        conn.close()


# Cria um objeto socket
sockobj = socket(AF_INET, SOCK_STREAM)
orig = (meuHost, minhaPorta)
sockobj.bind(orig)
sockobj.listen(5) # Aumentar um pouco o backlog é uma boa prática

print("Servidor pronto para receber conexões...")

# Loop principal agora apenas aceita conexões e dispara threads
while True:
    conn, cliente_addr = sockobj.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, cliente_addr))
    client_thread.start()