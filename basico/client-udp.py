# Importa todas as funções, classes e constantes do módulo socket da biblioteca padrão do Python.
from socket import *

# Define o endereço IP do servidor de destino. O endereço 127.0.0.1 (conhecido como localhost ou endereço de loopback) significa que o cliente irá se comunicar com um servidor que está rodando na mesma máquina. Se o servidor estivesse em outro computador na rede, este IP deveria ser colocado aqui.
meuHost = '127.0.0.1'

# Define a porta de destino no servidor. Este número deve ser o mesmo da porta em que o servidor está escutando.
minhaPorta = 5000

# Cria um objeto socket.
# AF_INET == protocolo de endereco IPv4.
# SOCK_DGRAM == protocolo de transferência UDP.
sockobj = socket(AF_INET, SOCK_DGRAM)

# OBS: Para o cliente não usamos o método .bind(). O sistema operacional se encarregará de escolher uma porta de origem livre e aleatória para enviar os pacotes.

# Cria uma tupla chamada dest que armazena o endereço completo do servidor (IP e porta). Esta tupla será usada para indicar para onde as mensagens devem ser enviadas.
dest = (meuHost, minhaPorta)

# Exibe uma instrução para o usuário sobre como encerrar o programa.
print('Para sair use CTRL+X\n')

# Inicializa a variável msg com uma string vazia. Isso é importante para que a condição do loop while possa ser avaliada na primeira vez sem erro.
msg = ''

# Inicia um loop que continuará executando enquanto o conteúdo da variável msg for diferente do caractere de controle Ctrl+X (\x18).
while msg != '\x18':

    # A função input() pausa a execução do programa e espera que o usuário digite uma mensagem no terminal e pressione Enter. O texto digitado é então armazenado na variável msg.
    msg = input()

    # Esta é a linha que efetivamente envia a mensagem pela rede.
    # sockobj.sendto(...): É o método usado para enviar um pacote UDP.
    # msg.encode(): A mensagem digitada pelo usuário (msg) é uma string. Soquetes enviam dados no formato de bytes, não strings de texto. O método .encode() converte a string para bytes (usando a codificação padrão UTF-8).
    # É o segundo argumento do método, indicando o endereço de destino (a tupla com o IP e a porta do servidor) para onde o pacote deve ser enviado.
    sockobj.sendto(msg.encode(), dest)

# Quando o usuário digita Ctrl+X e pressiona Enter, a condição do loop while se torna falsa e o loop termina. Esta linha é então executada, fechando o socket do cliente e liberando os recursos do sistema.
sockobj.close()