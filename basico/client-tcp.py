# Importa todas as funções, classes e constantes do módulo socket da biblioteca padrão do Python.
from socket import *

# Define o endereço IP do servidor de destino. O endereço 127.0.0.1 (conhecido como localhost ou endereço de loopback) significa que o cliente irá se comunicar com um servidor que está rodando na mesma máquina. Se o servidor estivesse em outro computador na rede, este IP deveria ser colocado aqui.
meuHost = '127.0.0.1'

# Define a porta de destino no servidor. Este número deve ser o mesmo da porta em que o servidor está escutando.
minhaPorta = 5001

# Cria um objeto socket.
# AF_INET == protocolo de endereco IPv4.
# SOCK_STREAM == protocolo de transferência TCP.
sockobj = socket(AF_INET, SOCK_STREAM)

# OBS: Para o cliente não usamos o método .bind(). O sistema operacional se encarregará de escolher uma porta de origem livre e aleatória para enviar os pacotes.

# Cria uma tupla chamada dest que armazena o endereço completo do servidor (IP e porta). Esta tupla será usada para indicar para onde as mensagens devem ser enviadas.
dest = (meuHost, minhaPorta)

# O método .connect() tenta estabelecer uma conexão direta com o servidor no endereço especificado em dest. Este processo é conhecido como three-way handshake no TCP, que garante que o servidor está pronto para receber dados. Se o servidor não estiver rodando ou a porta estiver errada, esta linha gerará um erro. Uma vez que a conexão é estabelecida, um canal de comunicação bidirecional está aberto entre o cliente e o servidor.
sockobj.connect(dest)

# Exibe uma instrução para o usuário sobre como encerrar o programa.
print('Para sair use CTRL+X\n')

# Inicializa a variável msg com uma string vazia. Isso é importante para que a condição do loop while possa ser avaliada na primeira vez sem erro.
msg = ''

# Inicia um loop que continuará executando enquanto o conteúdo da variável msg for diferente do caractere de controle Ctrl+X (\x18).
while msg != '\x18':

    # A função input() pausa a execução do programa e espera que o usuário digite uma mensagem no terminal e pressione Enter. O texto digitado é então armazenado na variável msg.
    msg = input()

    # Envia a mensagem para o servidor.
    # msg.encode(): Converte a string digitada pelo usuário para o formato de bytes, que é o formato necessário para transmissão pela rede.
    sockobj.send(msg.encode())

    # OBS: Note que usamos o método .send() em vez de .sendto(). Como a conexão TCP já foi estabelecida com .connect(), o socket "sabe" para onde enviar os dados. Não é necessário especificar o endereço de destino a cada envio.

# Quando o loop termina (após o usuário enviar Ctrl+X), esta linha é executada. O método .close() encerra formalmente a conexão TCP com o servidor e libera os recursos do sistema utilizados pelo socket.
sockobj.close()