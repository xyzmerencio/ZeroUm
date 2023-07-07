import subprocess


def bins():
    user_input = input("Digite o binário: ")
    url = f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{user_input}.md"
    output = f"{user_input}.txt"

    try:
        subprocess.run(['curl', '-o', output, url], check=True)
        print(f"Conteúdo salvo em {output}")
    except subprocess.CalledProcessError:
        print("Arquivo não encontrado ou erro na requisição")