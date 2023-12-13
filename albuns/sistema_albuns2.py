import os

def cadastrar_album():
    nome_album = input('Nome do álbum: ')
    ano_lancamento = input('Ano de lançamento: ')
    nome_artista = input('Nome da banda/artista: ')
    album_lancamento_artista = input('Álbum de lançamento do artista (sim/não): ')

    with open('albuns.txt', 'a') as file:
        file.write(f'{nome_album}|{ano_lancamento}|{nome_artista}|{album_lancamento_artista}\n')

def listar_albuns():
    if os.path.exists('albuns.txt') and os.path.getsize('albuns.txt') > 0:
        with open('albuns.txt', 'r') as file:
            for linha in file:
                dados = linha.strip().split('|')
                print(f'Nome do álbum: {dados[0]}')
                print(f'Ano de lançamento: {dados[1]}')
                print(f'Nome da banda/artista: {dados[2]}')
                print(f'Álbum de lançamento do artista: {dados[3]}')
                print('-' * 30)
    else:
        print('Nenhum álbum cadastrado.')

def busca_por_nome_artista(nome_procurado):
    albuns_encontrados = []
    with open('albuns.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split('|')
            nome_artista = dados[2]
            if nome_procurado.lower() in nome_artista.lower():
                albuns_encontrados.append(dados)
    return albuns_encontrados

def busca_por_ano(operador, ano_selecionado):
    albuns_encontrados = []
    with open('albuns.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split('|')
            ano_album = int(dados[1])
            if operador == "Anterior a" and ano_album <= ano_selecionado:
                albuns_encontrados.append(dados)
            elif operador == "Posterior a" and ano_album >= ano_selecionado:
                albuns_encontrados.append(dados)
            elif operador == "Igual a" and ano_album == ano_selecionado:
                albuns_encontrados.append(dados)
    return albuns_encontrados

def main():
    while True:
        print('\n1. Cadastrar álbum')
        print('2. Listar álbuns')
        print('3. Buscar por nome do artista')
        print('4. Buscar por ano do álbum')
        print('0. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_album()
        elif opcao == '2':
            listar_albuns()
        elif opcao == '3':
            nome_procurado = input('Digite o nome do artista: ')
            albuns_encontrados = busca_por_nome_artista(nome_procurado)
            print(f'\nÁlbuns do artista "{nome_procurado}":')
            for album in albuns_encontrados:
                print(album)
        elif opcao == '4':
            operador = input('Selecione o operador (Anterior a/Posterior a/Igual a): ')
            ano_selecionado = int(input('Digite o ano: '))
            albuns_encontrados = busca_por_ano(operador, ano_selecionado)
            print(f'\nÁlbuns do ano {operador} {ano_selecionado}:')
            for album in albuns_encontrados:
                print(album)
        elif opcao == '0':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
