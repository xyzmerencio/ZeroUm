import sys

PONTO = '.'
MAIS = '+'
TRACO = '-'
TRACO2 = '_'
combinacoes = []

def namelister(wordlist_file):
    """
    Gera uma wordlist com possíveis nomes de usuário com base em nomes reais em outra wordlist
    """
    with open(wordlist_file, "r", encoding='utf-8') as file:
        wordlist = [nome.strip() for nome in file.readlines()]

    for nome in wordlist:
        nome_parts = nome.split()
        primeiro_nome = nome_parts[0]
        sobrenome = nome_parts[1] if len(nome_parts) > 1 else ''

        combinacoes.append(primeiro_nome)
        combinacoes.append(sobrenome)
        combinacoes.append(primeiro_nome + sobrenome)
        combinacoes.append(primeiro_nome[0] + PONTO + sobrenome)
        combinacoes.append(primeiro_nome[0] + MAIS + sobrenome)
        combinacoes.append(primeiro_nome[0] + TRACO + sobrenome)
        combinacoes.append(primeiro_nome[0] + TRACO2 + sobrenome)
        combinacoes.append(primeiro_nome[:3] + sobrenome)
        combinacoes.append(primeiro_nome[:3] + PONTO + sobrenome)
        combinacoes.append(primeiro_nome[:3] + MAIS + sobrenome)
        combinacoes.append(primeiro_nome[:3] + TRACO + sobrenome)
        combinacoes.append(primeiro_nome[:3] + TRACO2 + sobrenome)
        combinacoes.append(primeiro_nome[:3] + PONTO + sobrenome[:3])
        combinacoes.append(primeiro_nome[:3] + MAIS + sobrenome[:3])
        combinacoes.append(primeiro_nome[:3] + TRACO + sobrenome[:3])
        combinacoes.append(primeiro_nome[:3] + TRACO2 + sobrenome[:3])
        combinacoes.append(sobrenome[:3] + PONTO + primeiro_nome[:3])
        combinacoes.append(sobrenome[:3] + MAIS + primeiro_nome[:3])
        combinacoes.append(sobrenome[:3] + TRACO + primeiro_nome[:3])
        combinacoes.append(sobrenome[:3] + TRACO2 + primeiro_nome[:3])

        if sobrenome:
            combinacoes.append(sobrenome[0] + primeiro_nome)
            combinacoes.append(primeiro_nome + PONTO + sobrenome[0])
            combinacoes.append(sobrenome[0] + PONTO + primeiro_nome)
            combinacoes.append(sobrenome + PONTO + sobrenome[0])
            combinacoes.append(primeiro_nome + MAIS + sobrenome[0])
            combinacoes.append(sobrenome[0] + MAIS + primeiro_nome)
            combinacoes.append(sobrenome + MAIS + sobrenome[0])
            combinacoes.append(primeiro_nome + TRACO + sobrenome[0])
            combinacoes.append(sobrenome[0] + TRACO + primeiro_nome)
            combinacoes.append(sobrenome + TRACO + sobrenome[0])
            combinacoes.append(primeiro_nome + TRACO2 + sobrenome[0])
            combinacoes.append(sobrenome[0] + TRACO2 + primeiro_nome)
            combinacoes.append(sobrenome + TRACO2 + sobrenome[0])

    with open("userslist.txt", "w", encoding='utf-8') as output_file:
        for comb in combinacoes:
            output_file.write(comb + '\n')

    print("Nomes salvos em userslist.txt")
