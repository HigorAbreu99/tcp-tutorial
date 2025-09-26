# Importa todas as funções, classes e constantes do módulo socket da biblioteca padrão do Python.
from socket import *

# Define o endereço IP do servidor de destino.
meuHost = '127.0.0.1'

# Define a porta de destino no servidor.
minhaPorta = 5001

# Cria um objeto socket.
sockobj = socket(AF_INET, SOCK_STREAM)

# Cria uma tupla chamada dest que armazena o endereço completo do servidor.
dest = (meuHost, minhaPorta)

# O método .connect() tenta estabelecer uma conexão direta com o servidor.
sockobj.connect(dest)

# Exibe uma instrução para o usuário sobre como encerrar o programa.
print('Para sair use CTRL+X e Enter\n')

# Inicializa a variável msg com uma string vazia.
msg = ''

# Inicia um loop que continuará executando enquanto a msg for diferente de Ctrl+X.
while msg != '\x18':

    # A função input() espera que o usuário digite uma mensagem.
    msg = input("Digite a mensagem: ")

    # Envia a mensagem para o servidor.
    sockobj.send(msg.encode())
    
    # Se a mensagem enviada for o sinal de saída, não espera por uma resposta.
    if msg == '\x18':
        break
        
    # Espera e recebe a resposta (eco) do servidor.
    data = sockobj.recv(1024)
    if not data:
        print("\nConexão fechada pelo servidor.")
        break
    
    # Imprime a resposta do servidor na tela.
    print('Eco do servidor:', data.decode())

# O método .close() encerra formalmente a conexão TCP com o servidor.
sockobj.close()