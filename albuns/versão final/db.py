import os

def cadastrar_album(nome_album, ano_lancamento, nome_artista, album_lancamento_artista):
    with open('albuns.txt', 'a') as file:
        file.write(f'{nome_album}|{ano_lancamento}|{nome_artista}|{album_lancamento_artista}\n')

def listar_albuns():
    albuns = []
    if os.path.exists('albuns.txt') and os.path.getsize('albuns.txt') > 0:
        with open('albuns.txt', 'r') as file:
            for linha in file:
                dados = linha.strip().split('|')
                albuns.append(dados)
    return albuns