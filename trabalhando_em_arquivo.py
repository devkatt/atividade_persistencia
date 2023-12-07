def cadastrar():
    while True:
        nome = input('Digite o seu nome (ou 0 para encerrar): ')
        
        if nome == "0":
            break  # Encerra o loop se o usuário digitar "0"
        
        idade = int(input('Digite sua idade: '))
        sexo = input('Digite o seu sexo (M ou F): ')
        telefone = input('Digite o seu telefone: ')

        with open('meu_nome.txt', 'a') as file:
            file.write(f'{nome}|{idade}|{sexo}|{telefone}\n')

def ler_dados():
    with open('meu_nome.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split('|')
            nome, idade, sexo, telefone = dados
            print(f'• Nome: {nome}')
            print(f'• Idade: {idade} anos')
            print(f'• Sexo: {"Masculino" if sexo == "M" else "Feminino"}')
            print(f'• Telefone: {telefone}')
            print()  # Adiciona uma linha em branco para separar as entradas

def busca_usuario_pelo_nome(nome_procurado):
    usuarios_encontrados = []
    with open('meu_nome.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split('|')
            nome_usuario = dados[0]
            if nome_procurado.lower() in nome_usuario.lower():
                usuarios_encontrados.append(dados)
    return usuarios_encontrados

def main():
    cadastrar()
    ler_dados()

    nome_desejado = input('Digite um nome ou parte dele para buscar: ')
    usuarios_encontrados = busca_usuario_pelo_nome(nome_desejado)
    
    print(f'\nUsuários com nome contendo "{nome_desejado}":')
    for usuario in usuarios_encontrados:
        print(usuario)

if __name__ == "__main__":
    main()
