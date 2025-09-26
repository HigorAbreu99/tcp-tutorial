from socket import *

meuHost = '127.0.0.1'
minhaPorta = 5001
sockobj = socket(AF_INET, SOCK_STREAM)
dest = (meuHost, minhaPorta)
sockobj.connect(dest)

print('Para sair use CTRL+X e Enter\n')

msg = ''

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