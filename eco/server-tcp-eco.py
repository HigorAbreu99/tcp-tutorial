# Importa todas as funções, classes e constantes do módulo socket da biblioteca padrão do Python.
from socket import *

# Define que o servidor escutará em todas as interfaces de rede da máquina.
meuHost = ''

# Define a porta de escuta como 5001.
minhaPorta = 5001

# Cria um objeto socket
# AF_INET == protocolo de endereco IPv4
# SOCK_STREAM == protocolo de transferência TCP
sockobj = socket(AF_INET, SOCK_STREAM)

# Cria uma tupla que combina o endereço do host e o número da porta.
orig = (meuHost, minhaPorta)

# O método .bind() vincula o socket ao endereço e porta especificados em orig.
sockobj.bind(orig)

# O método .listen() coloca o socket em modo de "escuta".
sockobj.listen(1)

# Inicia o loop principal do servidor.
while True:

    # O método .accept() é "bloqueante" e espera por uma conexão.
    conn, cliente = sockobj.accept()

    # Imprime uma mensagem no console informando que uma conexão foi estabelecida.
    print('Conectado por:', cliente)

    # Inicia um loop interno para gerenciar a troca de mensagens.
    while True:

        # Recebe os dados enviados pelo cliente.
        recvMsg = conn.recv(1024)

        # Verifica a condição para encerrar a comunicação.
        if recvMsg == b'\x18' or not recvMsg:
            break

        # Imprime a mensagem recebida no console do servidor.
        print(f"Recebido de {cliente}: {recvMsg.decode()}")
        
        # Envia a mesma mensagem de volta para o cliente (ECO).
        conn.send(recvMsg)

    # Este break faz com que o servidor atenda apenas um cliente e depois encerre.
    break

# Exibe uma mensagem de finalização e fecha o socket de conexão.
print('Finalizando conexão do cliente', cliente)
conn.close()