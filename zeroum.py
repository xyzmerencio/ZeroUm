from src.webcrawler.webcrawler import crawl_links
from src.emailfinder.emailfinder import crawl
from src.revshell.revshell import gerar_rev
from src.sshbrute.sshbrute import sshbrute
from src.ftpbrute.ftpbrute import ftpbrute
from src.dirbrute.dirbrute import dirbrute
from src.dnsbrute.dnsbrute import dnsbrute
from src.portscan.portscan import scan
from src.bins.bins import bins
import sys


print("""				 
        				          #
				                  &&
        #				          &&(
         @(				          &&%(
          @(/%				    &&@/(
           @@/(#%(    *..&&&&.,....... .  #&&@((#
            &&## ., @@@@@@@@&& ,,..,..  (%%&(#%
              /  @@@&@@@@&@@@@@@@,..... ####%#
               @@@@@&#@@@@&@@@@@@@@@@&(	,
              (@@@@@@%@%@@@@@@@@@@@@@&&##(	 #&/
             ##@@@@@@%@&@@@@@@@@@@@@@&&%#(// &@ /,#
             #&@@@@@@%@#@@@@@@@@@@@@@&&%#(//,@,*/.&
              @@@@@@#@#@@@@@@@@@@@@&&&%#(//&@.*##%
              &@@@@%(@@/%@@@@@@@@&&%#@##(###(/ #(
               ,#, ,(#,##//&.   *((#% /%###(/@//%
               /*& , %a@a// && .,&%@.#%%###(/,/.
             .@@@@@##.@&####@@@@@@@@@@&%(/(##(,
               &%%%#&@@@%%,%.*%@@&%%#&(@/%###(@
                /.* @@@@@@@&#(/((/%   # .%%###
                 @ @@*%% #/#/(##.. ..& %&%%%
                  &@%  (,  (# @%...,@%@&(%
                    .......... .. /@#&#@
                   ,% ,@a@ . &@  %%#/
                  %*,(@&/,. . ,@#%
                    %%##%%%%%%%(
        
        """)

def main():
    try:
        help_message = """
        Uso: python zeroum.py [opção] [argumentos]

        Opções:
        * -dir, --dirbrute      Executa um brute force de diretórios.
        * -ssh, --sshbrute      Executa um brute force SSH.
        * -ftp, --ftpbrute      Executa um brute force FTP.
        * -s, --portscan        Executa um scan de rede.
        * -dns, --dnsbrute      Executa um brute force de subdomínios.
        * -ef, --emails         Busca emails no site específicado.
        * -rev, --reverseshell  Gera uma reverse shell.
        * -wc, --webcrawler     Busca todos os links no site específicado.
        * -b, --bins            Formas de explorar o binário específicado.
        """

        if len(sys.argv) > 1:
            if sys.argv[1] == '-h' or sys.argv[1] == '--help':
                print(help_message)
            elif sys.argv[1] == '-ftp' or sys.argv[1] == '--ftpbrute':
                hostname = sys.argv[2] if len(sys.argv) > 2 else None
                username = sys.argv[3] if len(sys.argv) > 3 else None
                password = sys.argv[4] if len(sys.argv) > 4 else None

                if hostname and username and password:
                    ftpbrute()
                else:
                    print("Argumentos faltando. Utilize -ftp -h [hostname] -u [username] -p [senha]")
            elif sys.argv[1] == '-ssh' or sys.argv[1] == '--sshbrute':
                hostname = sys.argv[2] if len(sys.argv) > 2 else None
                username = sys.argv[3] if len(sys.argv) > 3 else None
                password = sys.argv[4] if len(sys.argv) > 4 else None

                if hostname and username and password:
                    sshbrute()
                else:
                    print("Argumentos faltando. Utilize -ssh -h [hostname] [-u username | -wu wordlist_usuarios] [-p senha | -wp wordlist_senhas]")
            elif sys.argv[1] == '-dir' or sys.argv[1] == '--dirbrute':
                url = sys.argv[2] if len(sys.argv) > 2 else None
                wordlist = sys.argv[3] if len(sys.argv) > 3 else None
                if url and wordlist:
                    with open(wordlist, "r") as file:
                        wordlist = file.readlines()
                    dirbrute(url, wordlist)
                else:
                    print("Argumentos faltando. Utilize -dir URL WORDLIST")
            elif sys.argv[1] == '-s' or sys.argv[1] == '--portscan':
                host = sys.argv[2] if len(sys.argv) > 2 else None
                porta_espec = sys.argv[3] if len(sys.argv) > 3 else None
                if host and porta_espec:
                    scan(host, porta_espec)
                else:
                    print("Argumentos faltando. Utilize -s HOST PORTA")
            elif sys.argv[1] == '-dns' or sys.argv[1] == '--dnsbrute':
                dominio = sys.argv[2] if len(sys.argv) > 2 else None
                wordlist = sys.argv[3] if len(sys.argv) > 3 else None
                if dominio and wordlist:
                    dnsbrute(dominio, wordlist)
                else:
                    print("Argumentos faltando. Utilize -dns DOMINIO WORDLIST")
            elif sys.argv[1] == '-ef' or sys.argv[1] == '--emails':
                url = sys.argv[2] if len(sys.argv) > 2 else None
                if url:
                    crawl(url)
                else:
                    print("Argumentos faltando. Utilize -ef URL")
            elif sys.argv[1] == '-wc' or sys.argv[1] == '--webcrawler':
                url = sys.argv[2] if len(sys.argv) > 2 else None
                if url:
                    crawl_links(url)
                else:
                    print("Argumentos faltando. Utilize -wc URL")
            elif sys.argv[1] == '-rev' or sys.argv[1] == '--reverseshell':
                gerar_rev()
            elif sys.argv[1] == '-b' or sys.argv[1] == '--bins':
                bins()
            else:
                print("Opção inválida.")
        else:
            print(help_message)
    
    except Exception as error:
        print("Ocorreu o seguinte erro:\n\n\n", error)
    except KeyboardInterrupt:
        print("\n\n\n Tchau :)")
        sys.exit(0)

main()
