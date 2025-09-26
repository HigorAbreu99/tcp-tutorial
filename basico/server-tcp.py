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

# O método .bind() vincula o socket ao endereço e porta especificados em orig. A partir deste momento, o sistema operacional sabe que qualquer pacote TCP que chegar na porta 5001 deve ser direcionado para este programa.
sockobj.bind(orig)

# O método .listen() coloca o socket em modo de "escuta", permitindo que ele aceite conexões de clientes.
# O número 1 indica o tamanho da "fila de espera" (backlog). Significa que, se o servidor estiver ocupado tratando uma conexão, ele pode enfileirar até 1 nova conexão pendente.
sockobj.listen(1)

# Inicia o loop principal do servidor, que ficará aguardando por novas conexões.
while True:

    # O método .accept() é "bloqueante", ou seja, o programa para aqui e espera até que um cliente tente se conectar.
    # Quando um cliente se conecta, .accept() retorna duas coisas:
    # conn: Um novo objeto socket. Este novo socket é o canal de comunicação direto e exclusivo com o cliente que acabou de se conectar. Toda a troca de dados (envio e recebimento) com este cliente específico será feita através de conn.
    # cliente: Uma tupla com o endereço IP e a porta do cliente conectado.
    conn, cliente = sockobj.accept()

    # Imprime uma mensagem no console informando que uma conexão foi estabelecida e de onde ela veio.
    print('Conectado por:', cliente)

    # Inicia um loop interno. Este loop é responsável por gerenciar a troca de mensagens com o cliente que está atualmente conectado.
    while True:

        # Recebe os dados enviados pelo cliente. O 1024 é o tamanho máximo de dados (em bytes) a serem lidos de uma só vez.
        recvMsg = conn.recv(1024)

        # OBS: Note que usamos conn.recv() e não sockobj.recvfrom(). O método .recv() lê os dados do socket de conexão (conn), que representa o fluxo de dados TCP estabelecido. Como a conexão já existe, não é necessário receber o endereço do remetente a cada mensagem.

        # Verifica a condição para encerrar a comunicação com o cliente. Caso seja verdadeira, interrompe este loop interno, finalizando a sessão com o cliente atual.
        if recvMsg == b'\x18' or not recvMsg:
            break

        # Se a mensagem for válida, decodifica-a de bytes para string e a exibe no console, junto com o endereço do cliente.
        print(cliente, recvMsg.decode())

    # Este break pertence ao loop externo. Após sair do loop de comunicação (interno), esta linha é executada, fazendo com que o loop principal do servidor também termine. Isso significa que este servidor foi projetado para atender apenas um cliente e depois ser encerrado.    
    break

# Exibe uma mensagem de finalização e fecha o socket de conexão (conn) para liberar os recursos associados a essa comunicação específica.
print('Finalizando conexão do cliente', cliente)
conn.close()