import socket

# Pergunta ao usuário qual IP procurar
ip = input("Digite o endereço IP que deseja fazer o portscan: ")

# Define o intervalo de portas a serem escaneadas (1 a 65535)
portas = range(1, 65536)

# Percorre todas as portas definidas para o IP especificado
for porta in portas:
    # Cria um objeto socket para conexão TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1) # Define um timeout de 0.1 segundos para cada conexão
    
    # Tenta se conectar à porta especificada
    resultado = sock.connect_ex((ip, porta))
    
    # Se a conexão for bem sucedida, significa que a porta está aberta
    if resultado == 0:
        print(f"Porta {porta} aberta")
    
    # Fecha a conexão
    sock.close()

