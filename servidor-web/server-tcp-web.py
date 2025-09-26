# Importa todas as funções, classes e constantes do módulo socket da biblioteca padrão do Python.
from socket import *

# Define que o servidor escutará em todas as interfaces de rede da máquina.
meuHost = ''

# DICA: Altera a porta para 80, a porta padrão para serviços Web (HTTP).
minhaPorta = 80

# Cria um objeto socket usando IPv4 e TCP.
sockobj = socket(AF_INET, SOCK_STREAM)

# Cria uma tupla que combina o endereço do host e o número da porta.
orig = (meuHost, minhaPorta)

# Vincula o socket ao endereço e porta especificados.
sockobj.bind(orig)

# Coloca o socket em modo de "escuta" para aceitar conexões.
sockobj.listen(5) # Aumentado o backlog para um valor mais comum em servidores web.

print(f"Servidor web iniciado em http://{meuHost if meuHost else '127.0.0.1'}:{minhaPorta}")

# Inicia o loop principal do servidor.
while True:

    # O método .accept() espera por uma conexão de um cliente (navegador).
    # 'conn' é o novo socket para comunicação direta com o cliente.
    conn, cliente = sockobj.accept()

    # Imprime no console o endereço do cliente que se conectou.
    print('Conectado por:', cliente)
    
    # Recebe a requisição HTTP do navegador (até 1024 bytes).
    request = conn.recv(1024)
    print("Requisição recebida:\n", request.decode())

    # --- Construção da Resposta HTTP ---
    
    # 1. Corpo da resposta (o conteúdo HTML)
    corpo_html = """
    <html>
        <head>
            <title>Servidor TCP Web</title>
        </head>
        <body>
            <h1>Ola, Mundo!</h1>
            <p>Esta pagina foi servida por um servidor TCP em Python.</p>
        </body>
    </html>
    """

    # 2. Cabeçalho da resposta HTTP
    # A primeira linha 'HTTP/1.1 200 OK' indica sucesso.
    # 'Content-Type' informa ao navegador que o conteúdo é HTML.
    # A linha em branco (\r\n) é obrigatória para separar o cabeçalho do corpo.
    cabecalho_http = """HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

"""
    
    # 3. Monta a resposta final juntando o cabeçalho e o corpo
    resposta_final = cabecalho_http + corpo_html

    # Envia toda a resposta HTTP para o navegador, codificada em bytes.
    # Usamos sendall para garantir que todos os dados sejam enviados.
    conn.sendall(resposta_final.encode('utf-8'))

    # Fecha a conexão com o cliente atual para liberar os recursos.
    conn.close()

    # O 'break' do script original foi removido para que o servidor
    # possa atender múltiplos clientes, um após o outro.