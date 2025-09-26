from socket import *
import threading

def receive_messages(sock):
    """Função para receber mensagens do servidor em uma thread separada."""
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"\nMensagem recebida: {msg}")
            else:
                # Servidor fechou a conexão
                break
        except:
            break
    print("Conexão fechada pelo servidor.")
    sock.close()

meuHost = '127.0.0.1'
minhaPorta = 5001
sockobj = socket(AF_INET, SOCK_STREAM)
dest = (meuHost, minhaPorta)
sockobj.connect(dest)

print('Para sair use CTRL+X e Enter\n')

msg = ''

# AQUI, após a conexão, iniciamos a thread de recebimento
receiver_thread = threading.Thread(target=receive_messages, args=(sockobj,))
receiver_thread.daemon = True # Permite que o programa principal feche mesmo se a thread estiver rodando
receiver_thread.start()

# Loop principal para enviar mensagens
try:
    while True:
        msg = input()
        if msg == '\x18': # CTRL+X
            break
        sockobj.send(msg.encode())
except KeyboardInterrupt:
    print("\nFechando...")

sockobj.close()