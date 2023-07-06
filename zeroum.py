from src.emailfinder.emailfinder import crawl
from src.revshell.revshell import gerar_rev
from src.dirbrute.dirbrute import dirbrute
from src.dnsbrute.dnsbrute import dnsbrute
from src.portscan.portscan import scan
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
        * -s, --portscan        Executa um scan de rede.
        * -dns, --dnsbrute      Executa um brute force de subdomínios.
        * -ef, --emails         Busca emails no site específicado.
        * -rev, --reverseshell  Gera uma reverse shell.
        """

        if len(sys.argv) > 1:
            if sys.argv[1] == '-dir' or sys.argv[1] == '--dirbrute':
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
                crawl(url)
            elif sys.argv[1] == '-rev' or sys.argv[1] == '--reverseshell':
                gerar_rev()
            else:
                print("Opção inválida.")
        else:
            print(help_message)
    
    except Exception as error:
        print("Ocorreu o seguinte erro:\n\n\nerror")
    except KeyboardInterrupt:
        print("\n\n\n Tchau :)")
        sys.exit(0)

main()
