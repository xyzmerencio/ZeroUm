import subprocess


def bins():
    """    
    Solicita ao usuário um binário, baixa o conteúdo do link correspondente 
    e o salva em um arquivo de texto.
    """
    user_input = input("Digite o binário: ")
    url = f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{user_input}.md"
    output = f"{user_input}.txt"

    try:
        subprocess.run(['curl', '-o', output, url], check=True)
        print(f"Conteúdo salvo em {output}")
    except subprocess.CalledProcessError:
        print("Arquivo não encontrado ou erro na requisição")
