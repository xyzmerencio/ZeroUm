from src.webcrawler.webcrawler import crawl_links
from src.namelister.namelister import namelister
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
    """
    Função principal que executa as diferentes funcionalidades do programa com base nos argumentos de linha de comando.
    """
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
        * -nl --namelister      Gera uma lista de nomes com possíveis usuários
        """

        if len(sys.argv) > 1:  # Verifica se foram fornecidos argumentos de linha de comando.
            if sys.argv[1] == '-h' or sys.argv[1] == '--help':  # Verifica se a opção de ajuda foi selecionada.
                print(help_message)  # Exibe a mensagem de ajuda.
            elif sys.argv[1] == '-ftp' or sys.argv[1] == '--ftpbrute':  # Verifica se a opção de brute force FTP foi selecionada.
                hostname = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém o nome do host FTP.
                username = sys.argv[3] if len(sys.argv) > 3 else None  # Obtém o nome de usuário.
                password = sys.argv[4] if len(sys.argv) > 4 else None  # Obtém a senha.

                if hostname and username and password:  # Verifica se todos os argumentos necessários foram fornecidos.
                    ftpbrute()  # Executa o brute force FTP.
                else:
                    print("Argumentos faltando. Utilize -ftp -h [hostname] -u [username] -p [senha]")  # Exibe uma mensagem informando que os argumentos estão faltando.
            elif sys.argv[1] == '-ssh' or sys.argv[1] == '--sshbrute':  # Verifica se a opção de brute force SSH foi selecionada.
                hostname = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém o nome do host SSH.
                username = sys.argv[3] if len(sys.argv) > 3 else None  # Obtém o nome de usuário.
                password = sys.argv[4] if len(sys.argv) > 4 else None  # Obtém a senha.

                if hostname and username and password:  # Verifica se todos os argumentos necessários foram fornecidos.
                    sshbrute()  # Executa o brute force SSH.
                else:
                    print("Argumentos faltando. Utilize -ssh -h [hostname] [-u username | -wu wordlist_usuarios] [-p senha | -wp wordlist_senhas]")  # Exibe uma mensagem informando que os argumentos estão faltando.
            elif sys.argv[1] == '-dir' or sys.argv[1] == '--dirbrute':  # Verifica se a opção de brute force de diretórios foi selecionada.
                url = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém a URL do site a ser varrido.
                wordlist = sys.argv[3] if len(sys.argv) > 3 else None  # Obtém o caminho para o arquivo de lista de palavras-chave.

                if url and wordlist:  # Verifica se todos os argumentos necessários foram fornecidos.
                    with open(wordlist, "r", encoding='utf-8') as file:  # Abre o arquivo da lista de palavras-chave para leitura.
                        wordlist = file.readlines()  # Lê as linhas do arquivo e armazena na variável "wordlist".
                    dirbrute(url, wordlist)  # Executa o brute force de diretórios.
                else:
                    print("Argumentos faltando. Utilize -dir URL WORDLIST")  # Exibe uma mensagem informando que os argumentos estão faltando.
            elif sys.argv[1] == '-s' or sys.argv[1] == '--portscan':  # Verifica se a opção de scan de rede foi selecionada.
                host = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém o endereço IP do host.
                porta_espec = sys.argv[3] if len(sys.argv) > 3 else None  # Obtém a porta específica para scan.

                if host and porta_espec:  # Verifica se todos os argumentos necessários foram fornecidos.
                    scan(host, porta_espec)  # Executa o scan de rede.
                else:
                    print("Argumentos faltando. Utilize -s HOST PORTA")  # Exibe uma mensagem informando que os argumentos estão faltando.
            elif sys.argv[1] == '-dns' or sys.argv[1] == '--dnsbrute':  # Verifica se a opção de brute force de subdomínios foi selecionada.
                dominio = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém o domínio base para a busca.
                wordlist = sys.argv[3] if len(sys.argv) > 3 else None  # Obtém o caminho para o arquivo de lista de palavras-chave.

                if dominio and wordlist:  # Verifica se todos os argumentos necessários foram fornecidos.
                    dnsbrute(dominio, wordlist)  # Executa o brute force de subdomínios.
                else:
                    print("Argumentos faltando. Utilize -dns DOMINIO WORDLIST")  # Exibe uma mensagem informando que os argumentos estão faltando.
            elif sys.argv[1] == '-ef' or sys.argv[1] == '--emails':  # Verifica se a opção de busca de emails foi selecionada.
                url = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém o URL do site a ser varrido.

                if url:  # Verifica se o argumento necessário foi fornecido.
                    crawl(url)  # Executa a busca de emails no site especificado.
                else:
                    print("Argumentos faltando. Utilize -ef URL")  # Exibe uma mensagem informando que o argumento está faltando.
            elif sys.argv[1] == '-wc' or sys.argv[1] == '--webcrawler':  # Verifica se a opção de busca de todos os links foi selecionada.
                url = sys.argv[2] if len(sys.argv) > 2 else None  # Obtém o URL do site a ser varrido.

                if url:  # Verifica se o argumento necessário foi fornecido.
                    crawl_links(url)  # Executa a busca de todos os links no site especificado.
                else:
                    print("Argumentos faltando. Utilize -wc URL")  # Exibe uma mensagem informando que o argumento está faltando.
            elif sys.argv[1] == '-rev' or sys.argv[1] == '--reverseshell':  # Verifica se a opção de geração de uma reverse shell foi selecionada.
                gerar_rev()  # Executa a geração da reverse shell.
            elif sys.argv[1] == '-nl' or sys.argv[1] == '--namelister':  # Verifica se a opção de geração de uma lista de nomes com possíveis usuários foi selecionada.
                namelister(sys.argv[2])  # Executa a geração da lista de nomes com possíveis usuários.
            elif sys.argv[1] == '-b' or sys.argv[1] == '--bins':  # Verifica se a opção de formas de explorar um binário foi selecionada.
                bins()  # Executa a exploração do binário especificado.
            else:
                print("Opção inválida.")  # Exibe uma mensagem informando que a opção selecionada é inválida.
        else:
            print(help_message)  # Exibe a mensagem de ajuda caso não sejam fornecidos argumentos de linha de comando.
    
    except Exception as error:
        print("Ocorreu o seguinte erro:\n\n\n", error)  # Exibe uma mensagem informando o erro que ocorreu.
    except KeyboardInterrupt:
        print("\n\n\n Tchau :)")  # Exibe uma mensagem de despedida caso a execução seja interrompida pelo usuário.
        sys.exit(0)  # Encerra o programa.

main()  # Chama a função principal para iniciar o programa.
