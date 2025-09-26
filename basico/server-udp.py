# Importa todas as funções, classes e constantes do módulo socket da biblioteca padrão do Python.
from socket import *

# Ao usar uma string vazia para 'meuHost', o servidor se torna "escutável" em todas as interfaces de rede disponíveis na máquina (por exemplo, localhost, o IP da rede local, etc.).
meuHost = ''

# Define como 5000 o número da porta em que o servidor irá "escutar" por mensagens.
minhaPorta = 5000

# Cria um objeto socket.
# AF_INET == protocolo de endereco IPv4.
# SOCK_DGRAM == protocolo de transferência UDP.
sockobj = socket(AF_INET, SOCK_DGRAM)

# Cria uma tupla que combina o endereço do host e o número da porta.
orig = (meuHost, minhaPorta)

# O método .bind() vincula o socket ao endereço e porta especificados em orig. A partir deste momento, o sistema operacional sabe que qualquer pacote UDP que chegar na porta 5000 deve ser direcionado para este programa.
sockobj.bind(orig)

# Inicia um loop infinito, fazendo com que o servidor rode continuamente, esperando por novas mensagens, até que uma condição de parada seja encontrada dentro do loop.
while True:

    # Este método faz o programa pausar e esperar até que uma mensagem chegue na porta vinculada. 
    # O 1024 é o tamanho em bytes do buffer. Se a mensagem possuir mais que 1024 bytes, ela será truncada.
    # O método retorna duas coisas: os dados da mensagem recebida em bytes e uma tupla contendo o endereço IP e a porta do cliente que enviou a mensagem.
    recvMsg, cliente = sockobj.recvfrom(1024)

    # Se receber um Ctrl + X ou mensagem vazia, para o loop e fecha o servidor
    if recvMsg == b'\x18' or not recvMsg:
        break

    # Se a condição de parada não for atendida, esta linha processa a mensagem recebida
    # recvMsg.decode(): Converte a mensagem de bytes (que é como os dados são transmitidos pela rede) para uma string de texto legível (usando a codificação padrão UTF-8). Isso permite que o texto da mensagem seja exibido corretamente no terminal.
    print(cliente, recvMsg.decode())

# O método .close() fecha o socket, liberando a porta 5000 e outros recursos do sistema que estavam sendo usados pelo programa
sockobj.close()